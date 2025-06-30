# models.py

"""
Contains models for signal propagation and building attenuation.

Includes:
- Log-distance path loss model
- Concrete slab attenuation
"""

import numpy as np

def log_distance_path_loss(frequency_mhz, distance_m, reference_distance_m=1.0, path_loss_exponent=2.7):
    """
    Computes the path loss (in dB) using the log-distance model.

    Parameters:
        frequency_mhz (float): Frequency in MHz (e.g., 868)
        distance_m (float): Distance from transmitter in meters
        reference_distance_m (float): Reference distance (usually 1m)
        path_loss_exponent (float): Environment-specific factor

    Returns:
        float: Path loss in dB
    """
    if distance_m < reference_distance_m:
        distance_m = reference_distance_m

    # Free-space path loss at reference distance
    fspl = 20 * np.log10(reference_distance_m) + 20 * np.log10(frequency_mhz) + 32.44
    path_loss = fspl + 10 * path_loss_exponent * np.log10(distance_m / reference_distance_m)
    return path_loss

def total_concrete_loss(num_floors, slab_loss_db):
    """
    Calculates total attenuation due to concrete floor slabs.

    Parameters:
        num_floors (int): Number of concrete slabs between Tx and Rx
        slab_loss_db (float): Attenuation per slab (in dB)

    Returns:
        float: Total attenuation in dB
    """
    return num_floors * slab_loss_db
