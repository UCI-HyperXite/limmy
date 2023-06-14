# limmy

a VESC communication library for python with an emphasis on simplicity and ease of use for Linear Induction Motors

## Installation

To use limmy, you must first install a few libraries:

```bash
pip install pyserial
pip install crcmod
```

Then, to use limmy, you can simply copy the limmy module folder into your project directory and import it like so:

```python
import limmy
```

## General Usage

Limmy is designed to be as simple as possible to use. To create a limmy object, simply call the limmy constructor with the port name of your VESC:

```python
motor = limmy.VESC(serial_port="COM3")
```

From there on, you can call upon the built in functions that abstract the control of the connected VESC.

## Example for Rotoary Motors

To control rotational motors, several functions are available:

```python
motor.set_speed_mph(10) # Sets the motor to 10 MPH
motor.set_rpm(1000) # Sets the motor to 1000 RPM
motor.set_current(10) # Sets the motor to 10 Amps
motor.set_duty_cycle(0.5) # Sets the motor to 50% duty cycle
motor.halt() # Stops the motor
```

## Example for Linear Motors

To control explicitly control linear induction motors, a function is provided

```python
motor.engage(I,f) # Engages the motor with current I and frequency f
motor.halt() # Stops the motor
```

This function is designed to be used in a loop, where the frequency is changed in accordance with the current mechanical speed. An important aspect of using a LIM for propulsion is that the synchronous speed of the stator field (defined by the frequency) must be greater than the mechanical speed of the motor. This is because the rotor will always be dragged along by the stator field, and if the stator field is moving slower than the rotor, the rotor will act as a brake.

## Example for Reading Data

Limmy also provides several functions for reading data from the VESC:

```python
motor.get_v_in() # Returns the input voltage
motor.get_motor_current() # Returns the current through the motor
motor.get_incoming_current() # Returns the current coming into the VESC
motor.get_firmware_version() # Returns the firmware version of the VESC (Should return a nonzero value if the VESC is connected)
```

## Acknowledgements

Limmy was written by [Adrian Ornelas](https://afornelas.com/) for the HyperXite 8 team at UC Irvine.

This library was inspired and based on [PyVESC](https://github.com/LiamBindle/PyVESC) by Liam Bindle. However, PyVESC is no longer maintained and is not compatible with the latest VESC firmware and python version. Limmy is designed to be a simple and easy to use library for controlling VESC's with the latest firmware and Python 3.8+ painlessly.

I'd like to thank the HyperXite 8 team for their support and encouragement in the development of this library.

With a special thanks to:

- Amanda Lieng
- Saketh Karumuri
- Lea Pang
- Taesung Hwang
