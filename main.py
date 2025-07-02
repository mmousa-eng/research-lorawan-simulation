# main.py

import yaml
from device import LoRaDevice  # Your device.py defining LoRaDevice class
from simulate import simulate_signal  # Your simulate.py with signal calc
from plot import plot_rssi_vs_floor  # Your updated plot.py
import argparse

def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def print_reachability_report(rssi_results, sensitivity_dbm):
    """
    Prints a floor-by-floor reachability report based on RSSI values.

    Parameters:
        rssi_results (list of tuples): List of (floor, RSSI in dBm)
        sensitivity_dbm (float): Receiver sensitivity threshold in dBm
    """
    print("\n=== LoRaWAN Signal Reachability Report ===")
    for floor, rssi in rssi_results:
        status = "Reachable" if rssi >= sensitivity_dbm else "Not reachable"
        print(f"Floor {floor}: RSSI = {rssi:.1f} dBm --> {status}")
    print("==========================================\n")

def parse_args():
    parser = argparse.ArgumentParser(description="LoRaWAN Signal Simulation")
    parser.add_argument("--config", type=str, default="config.yaml",
                        help="Path to configuration YAML file")
    return parser.parse_args()

def main():
    args = parse_args()
    config = load_config(args.config)

    # Initialize LoRa device from config parameters
    device_cfg = config["lorawan_device"]
    device = LoRaDevice(
        frequency_mhz=device_cfg["frequency_mhz"],
        tx_power_dbm=device_cfg["tx_power_dbm"],
        bandwidth_khz=device_cfg["bandwidth_khz"],
        spreading_factor=device_cfg["spreading_factor"],
        receiver_sensitivity_dbm=device_cfg["receiver_sensitivity_dbm"]
    )

    # Extract building and environment parameters
    building_cfg = config["building"]
    env_cfg = config["environment"]
    floor_height = building_cfg.get("floor_height_m", 3)
    slab_attenuation = building_cfg.get("slab_attenuation_db", 15)
    path_loss_exp = env_cfg.get("path_loss_exponent", 2.0)
    reference_distance = env_cfg.get("reference_distance_m", 1.0)

    # Simulate RSSI from rooftop (floor N) down to basement (floor 0)
    floors = list(range(building_cfg["num_floors"], -1, -1))  # e.g., 6 to 0
    rssi_results = simulate_signal(
        device, floors,
        floor_height_m=floor_height,
        slab_attenuation_db=slab_attenuation,
        path_loss_exponent=path_loss_exp,
        reference_distance_m=reference_distance
    )

    # Simulate for both 868 MHz and 433 MHz
    device_868 = LoRaDevice(
        frequency_mhz=868,
        tx_power_dbm=device_cfg["tx_power_dbm"],
        bandwidth_khz=device_cfg["bandwidth_khz"],
        spreading_factor=device_cfg["spreading_factor"],
        receiver_sensitivity_dbm=device_cfg["receiver_sensitivity_dbm"]
    )
    device_433 = LoRaDevice(
        frequency_mhz=433,
        tx_power_dbm=device_cfg["tx_power_dbm"],
        bandwidth_khz=device_cfg["bandwidth_khz"],
        spreading_factor=device_cfg["spreading_factor"],
        receiver_sensitivity_dbm=device_cfg["receiver_sensitivity_dbm"]
    )

    # Simulate RSSI for both frequencies
    rssi_results_868 = simulate_signal(
        device_868, floors,
        floor_height_m=floor_height,
        slab_attenuation_db=slab_attenuation,
        path_loss_exponent=path_loss_exp,
        reference_distance_m=reference_distance
    )
    rssi_results_433 = simulate_signal(
        device_433, floors,
        floor_height_m=floor_height,
        slab_attenuation_db=slab_attenuation,
        path_loss_exponent=path_loss_exp,
        reference_distance_m=reference_distance
    )

    # Print reachability report for both
    print("\n--- 868 MHz ---")
    print_reachability_report(rssi_results_868, device_868.receiver_sensitivity_dbm)
    print("\n--- 433 MHz ---")
    print_reachability_report(rssi_results_433, device_433.receiver_sensitivity_dbm)

    # Plot both on the same figure
    plot_rssi_vs_floor(rssi_results_868, rssi_results_433, device_868.receiver_sensitivity_dbm)

if __name__ == "__main__":
    main()
