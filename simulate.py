# simulate.py

"""
Runs the signal simulation from rooftop to basement in a multi-storey building.
"""

from models import log_distance_path_loss, total_concrete_loss

def simulate_signal(device, config):
    """
    Simulates RSSI from roof (floor N) to basement (floor 0).

    Parameters:
        device (LoRaDevice): The transmitting device with its parameters
        config (dict): Loaded YAML config with building and environment info

    Returns:
        list of tuples: [(floor, RSSI in dBm), ...]
    """
    num_floors = config["building"]["num_floors"]
    floor_height = config["building"]["floor_height_m"]
    slab_loss = config["building"]["slab_attenuation_db"]
    path_loss_exp = config["environment"]["path_loss_exponent"]
    reference_d = config["environment"]["reference_distance_m"]
    freq_mhz = device.frequency_mhz

    results = []

    for floor in range(num_floors, -1, -1):  # from top (6) to bottom (0)
        vertical_distance = (num_floors - floor) * floor_height
        path_loss = log_distance_path_loss(
            frequency_mhz=freq_mhz,
            distance_m=vertical_distance,
            reference_distance_m=reference_d,
            path_loss_exponent=path_loss_exp,
        )
        slab_count = num_floors - floor
        total_loss = path_loss + total_concrete_loss(slab_count, slab_loss)

        rssi = device.tx_power_dbm - total_loss
        results.append((floor, round(rssi, 2)))

    return results
