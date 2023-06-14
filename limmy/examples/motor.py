import limmy
import time

# How to use limmy, by Adrian Ornelas

# First, create a motor object. This will automatically start the heartbeat thread that keeps the motor alive.

serial_port = 'COM15' # Change this to the serial port of your VESC, on Linux (Raspberry Pi) it will be something like '/dev/ttyUSB0'
motor = limmy.VESC(serial_port=serial_port)
print("Firmware: ", motor.get_firmware_version())
time.sleep(1)

# Motor can be started via motor.engage command:
    # The utilization for the command is: motor.engage(current, rpm)
    # Where current is in Amps and is a float above 0.0
    # And frequency is in Hz and is an float above 0.0

motor.engage(30, 30)
time.sleep(5)

# Similarly, the motor can be stopped via the motor.halt command:
motor.halt(0)
time.sleep(1)

# You can also poll relevent data from the motor:

motor.get_v_in() # Input voltage to the Flipsky VESC, should match Orion BMS 2 Pack Voltage, roughly 44~48V
motor.get_motor_current() # Current being drawn by the motor, informs force output
motor.get_incoming_current() # Current being drawn from the battery, should match Orion BMS 2 Pack Current


# Lastly, remember to stop the heartbeat thread before the object goes out of scope:
    # Failing to do so will mean the thread will continue to run in the background, 
    # even if the program has ended, and the motor will not be able to be controlled
    # until the python runtime is fully restarted.
motor.stop_heartbeat()


'''
High Voltage System Electrical Diagram:

Note that each 44V Battery should be equppied with a 50 Amp fuse, High Current Switch
and unique contactor. The contactors should be controlled by the Raspberry Pi such that the
High Voltage system is always OFF when the Raspberry Pi is not running.

The Flipsky VESC's and Orion BMS 2 are connected to the Raspberry Pi via USB Serial.

In the future, both the VESC and BMS should be connected to the Raspberry Pi via CAN Bus. (TODO HX9)

Remember to always wear appropriate PPE when working with High Voltage systems,
and to always work with a partner. For any questions, contact Adrian or Saketh.

 ┌───────────────┐         ┌─────────────────┐
 │               │         │                 │
 │ 44V Battery 1 ├────────►│  Flipsky VESC 1 ├──┐
 │               │         │                 │  │
 └───────┬───────┘         └─────────────────┘  │ ┌────────────┐
         │                                      └►│LIM L       │
         │     ┌──────────────┐                   ├────────────┤
         │     │              │         ┌─────────┴────────────┴─────────────┐
         ├────►│ Orion BMS 2  │         │ I-Beam Rotor                       │
         │     │              │         └─────────┬────────────┬─────────────┘
         │     └──────────────┘                   ├────────────┤
         │                                      ┌►│LIM R       │
 ┌───────┴───────┐         ┌─────────────────┐  │ └────────────┘
 │               │         │                 │  │
 │ 44V Battery 2 ├────────►│  Flipsky VESC 2 ├──┘
 │               │         │                 │
 └───────────────┘         └─────────────────┘
 '''