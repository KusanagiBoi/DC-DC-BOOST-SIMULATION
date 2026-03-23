# DC-DC Boost Converter Simulation

Mathematical model and numerical simulation for Power Electronics analysis, focusing on the dynamics of a boost power stage.

---

## Engineering Analysis

This tool is designed to evaluate the transfer functions and steady-state behavior of a DC-DC boost converter using Python. It allows for direct manipulation of the mathematical parameters that govern power conversion, providing a deeper look into the system's physics than traditional SPICE-based black-box simulations.

### Theoretical Foundation

The simulation implements the fundamental boost converter voltage gain equation:

$$V_{out} = \frac{V_{in}}{1 - D}$$

Where:
* **$V_{in}$**: Input Voltage (V)
* **$D$**: Duty Cycle ($0 \leq D < 1$)
* **$V_{out}$**: Output Voltage (V)

---

## Technical Features

* **Transient & Steady-State Analysis**: Simulates the voltage climb and stabilization phase based on inductor ($L$) and capacitor ($C$) time constants.
* **Ripple Calculation**: Precise analysis of inductor current ripple ($\Delta I_L$) and output voltage ripple ($\Delta V_{out}$) to assist in component selection.
* **Non-Ideal Effects**: Capability to factor in ESR (Equivalent Series Resistance) of the inductor and conduction losses in the switching elements.

### Tech Stack
* **Language**: Python 3.x
* **Numerical Processing**: NumPy (Matrix operations and numerical integration)
* **Data Visualization**: Matplotlib (High-fidelity waveform generation)

---

## Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/KusanagiBoi/DC-DC-BOOST-SIMULATION.git](https://github.com/KusanagiBoi/DC-DC-BOOST-SIMULATION.git)
   cd DC-DC-BOOST-SIMULATION

2. **Setup Environment**:
   It is recommended to use a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt

3. **Run Simulation**:
   ```bash
   python main.py

This project is licensed under the MIT License
   
