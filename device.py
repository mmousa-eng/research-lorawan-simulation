# device.py

"""
Defines the LoRaDevice class with transmission and sensor parameters.
"""

class Sensor:
    def __init__(self, name, data_rate_bps):
        self.name = name
        self.data_rate_bps = data_rate_bps  # For future use (e.g., flow sensor: 9600bps)

    def __repr__(self):
        return f"{self.name} ({self.data_rate_bps} bps)"

class LoRaDevice:
    def __init__(self, tx_power_dbm, spreading_factor, bandwidth_khz, frequency_mhz, receiver_sensitivity_dbm):
        self.tx_power_dbm = tx_power_dbm
        self.spreading_factor = spreading_factor
        self.bandwidth_khz = bandwidth_khz
        self.frequency_mhz = frequency_mhz
        self.receiver_sensitivity_dbm = receiver_sensitivity_dbm
        self.sensors = []

    def add_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def print_config(self):
        print("LoRa Device Configuration:")
        print(f"  Tx Power: {self.tx_power_dbm} dBm")
        print(f"  Spreading Factor: SF{self.spreading_factor}")
        print(f"  Bandwidth: {self.bandwidth_khz} kHz")
        print(f"  Frequency: {self.frequency_mhz} MHz")
        print(f"  Receiver Sensitivity: {self.receiver_sensitivity_dbm} dBm")
        print("  Connected Sensors:")
        for sensor in self.sensors:
            print(f"    - {sensor}")
