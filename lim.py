import limmy
import time

serial_port_1 = '/dev/tty.usbmodem3'
serial_port_2 = '/dev/tty.usbmodem3041'

print('[INFO] Initializing motor 1 on port: ', serial_port_1)
motor_1 = limmy.VESC(serial_port=serial_port_1)
print('[INFO] Initializing motor 2 on port: ', serial_port_2)
motor_2 = limmy.VESC(serial_port=serial_port_2)

print("Firmware 1: ", motor_1.get_firmware_version())
print("Firmware 2: ", motor_2.get_firmware_version())
time.sleep(1)

f = 30
I = 30

val = True
run = True
direction = True

input('[INFO] Wait for input to start')

def safe_stop():
    try:
        motor_1.halt()
    except Exception:
        pass
    try:
        motor_2.halt()
    except Exception:
        pass

def auto_cycle():
    print('Auto-cycle starting for 100 seconds. Switching every 2.75s.')
    auto_direction = True
    end_time = time.time() + 100.0
    try:
        while time.time() < end_time:
            if auto_direction:
                motor_2.halt()
                motor_1.engage(I, f)
            else:
                motor_1.halt()
                motor_2.engage(I, f)
            auto_direction = not auto_direction
            time.sleep(2.75)
    except Exception as e:
        print(f'[WARNING] Auto-cycle interrupted: {e}')
    finally:
        safe_stop()
        print('[INFO] Auto-cycle complete. Motors halted.')

while run:
    if direction:
        motor_2.halt()
        motor_1.engage(I, f)
        direction = False
    else:
        motor_1.halt()
        motor_2.engage(I, f)
        direction = True

    val = input("Enter: Change directions | Space: Change parameters | a: Auto-cycle | Any other key: Abort\n> ")

    if val == ' ':
        safe_stop()
        I = float(input("Enter current: "))
        val = ''
    elif val == 'a':
        safe_stop()
        auto_cycle()
        run = False
    elif val != '':
        run = False

safe_stop()

time.sleep(1)

try:
    motor_1.stop_heartbeat()
except Exception:
    pass
try:
    motor_2.stop_heartbeat()
except Exception:
    pass