# 🔍 Research: LoRaWAN Building Penetration Simulation

This project simulates the signal reach of a LoRaWAN device placed on the rooftop of a 6-storey concrete building, estimating the received signal strength (RSSI) at each floor down to the basement.
Technologies: Python • Matplotlib • PyYAML • Signal Processing • LoRaWAN Simulation

## Goals
- Model LoRaWAN signal propagation through concrete floors
- Visualize RSSI per floor and compare to device sensitivity
- Allow easy configuration of parameters (floors, power, attenuation, etc.)

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Edit `config.yaml` to set simulation parameters.
3. Run the simulation:
   ```bash
   python main.py
   ```
4. View the generated RSSI plot.

## File Structure
- `device.py`: LoRaDevice class
- `models.py`: Signal propagation models
- `simulate.py`: RSSI calculation logic
- `plot.py`: Plotting utilities
- `main.py`: Orchestrates config, simulation, and plotting
- `config.yaml`: Simulation parameters
