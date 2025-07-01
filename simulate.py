# simulate.py

"""
Runs the signal simulation from rooftop to basement in a multi-storey building.
"""

from models import log_distance_path_loss, total_concrete_loss

def simulate_signal(device, floors, floor_height_m=3.0, slab_attenuation_db=15.0, path_loss_exponent=2.0, reference_distance_m=1.0):
    """
    Simulates RSSI from roof (floor N) to basement (floor 0).

    Parameters:
        device (LoRaDevice): The transmitting device with its parameters
        floors (list): List of floor numbers (e.g., [6,5,4,3,2,1,0])
        floor_height_m (float): Height per floor in meters
        slab_attenuation_db (float): Attenuation per floor slab in dB
        path_loss_exponent (float): Path loss exponent for environment
        reference_distance_m (float): Reference distance for path loss (m)

    Returns:
        list of tuples: [(floor, RSSI in dBm), ...]
    """
    freq_mhz = device.frequency_mhz
    num_floors = max(floors)
    results = []
    for floor in floors:
        vertical_distance = (num_floors - floor) * floor_height_m
        path_loss = log_distance_path_loss(
            frequency_mhz=freq_mhz,
            distance_m=max(vertical_distance, reference_distance_m),
            reference_distance_m=reference_distance_m,
            path_loss_exponent=path_loss_exponent,
        )
        slab_count = num_floors - floor
        total_loss = path_loss + total_concrete_loss(slab_count, slab_attenuation_db)
        rssi = device.tx_power_dbm - total_loss
        results.append((floor, round(rssi, 2)))
    return results
