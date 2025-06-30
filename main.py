# main.py

"""
Main entry point to run LoRaWAN signal simulation in a concrete building.
Loads config, creates device, runs simulation, and plots results.
"""

import yaml
from device import LoRaDevice
from simulate import simulate_signal
from plot import plot_rssi_vs_floor

def load_config(path='config.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()

    device_cfg = config['lorawan_device']
    device = LoRaDevice(
        tx_power_dbm=device_cfg['tx_power_dbm'],
        spreading_factor=device_cfg['spreading_factor'],
        bandwidth_khz=device_cfg['bandwidth_khz'],
        frequency_mhz=device_cfg['frequency_mhz'],
        receiver_sensitivity_dbm=device_cfg['receiver_sensitivity_dbm']
    )

    print("Running LoRaWAN Signal Simulation...")
    device.print_config()

    rssi_results = simulate_signal(device, config)

    print("\nRSSI Results (Floor : RSSI dBm):")
    for floor, rssi in rssi_results:
        print(f"Floor {floor}: {rssi} dBm")

    plot_rssi_vs_floor(rssi_results, device.receiver_sensitivity_dbm)

if __name__ == '__main__':
    main()
