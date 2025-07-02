# plot.py

"""
Plot RSSI vs building floor with receiver sensitivity threshold.
"""

import matplotlib.pyplot as plt
import os

def plot_rssi_vs_floor(rssi_data_868, rssi_data_433, receiver_sensitivity_dbm):
    """
    Plots RSSI per floor for both 868 MHz and 433 MHz, and marks the receiver sensitivity.

    Parameters:
        rssi_data_868 (list of tuples): [(floor, RSSI), ...] for 868 MHz
        rssi_data_433 (list of tuples): [(floor, RSSI), ...] for 433 MHz
        receiver_sensitivity_dbm (float): Receiver sensitivity threshold in dBm
    """
    floors_868, rssi_values_868 = zip(*rssi_data_868)
    floors_433, rssi_values_433 = zip(*rssi_data_433)

    plt.figure(figsize=(8, 5))
    plt.plot(floors_868, rssi_values_868, marker='o', linestyle='-', color='b', label='RSSI 868 MHz')
    plt.plot(floors_433, rssi_values_433, marker='s', linestyle='-', color='g', label='RSSI 433 MHz')
    plt.axhline(y=receiver_sensitivity_dbm, color='r', linestyle='--', label='Receiver Sensitivity')
    
    plt.gca().invert_xaxis()  # Optional: invert X to show top floor on left
    plt.xticks(floors_868)
    plt.xlabel('Floor Level (0 = Basement, Higher = Roof)')
    plt.ylabel('RSSI (dBm)')
    plt.title('LoRaWAN Signal Strength vs Floor Level (868 MHz vs 433 MHz)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Create output folder if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "simulation_plot_868_vs_433.png")
    
    plt.savefig(output_path)
    print(f"Plot saved as {output_path}")

    plt.show()
