# plot.py

"""
Plot RSSI vs building floor with receiver sensitivity threshold.
"""

import matplotlib.pyplot as plt
import os

def plot_rssi_vs_floor(rssi_data, receiver_sensitivity_dbm):
    """
    Plots RSSI per floor and marks the receiver sensitivity.

    Parameters:
        rssi_data (list of tuples): [(floor, RSSI), ...]
        receiver_sensitivity_dbm (float): Receiver sensitivity threshold in dBm
    """
    floors, rssi_values = zip(*rssi_data)

    plt.figure(figsize=(8, 5))
    plt.plot(floors, rssi_values, marker='o', linestyle='-', color='b', label='RSSI (dBm)')
    plt.axhline(y=receiver_sensitivity_dbm, color='r', linestyle='--', label='Receiver Sensitivity')
    
    plt.gca().invert_xaxis()  # Optional: invert X to show top floor on left
    plt.xticks(floors)
    plt.xlabel('Floor Level (0 = Basement, Higher = Roof)')
    plt.ylabel('RSSI (dBm)')
    plt.title('LoRaWAN Signal Strength vs Floor Level')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Create output folder if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "simulation_plot.png")
    
    plt.savefig(output_path)
    print(f"Plot saved as {output_path}")

    plt.show()
