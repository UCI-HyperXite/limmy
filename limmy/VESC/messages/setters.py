from limmy.protocol.base import VESCMessage
from limmy.protocol.interface import encode
from limmy.VESC.messages import VedderCmd

class SendTerminalCMD(metaclass=VESCMessage):
    id = VedderCmd.COMM_TERMINAL_CMD
    fields = [
        ('cmd','s')
    ]

class SetGPDFreq(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_SET_FSW
    fields = [
        ('frequency','i',1)
    ]

class SetGPDMode(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_SET_MODE
    fields = [
        ('mode','i',1)
    ]

class SetGPDOutputSample(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_OUTPUT_SAMPLE
    fields = [
        ('sample','f',1)
    ]

class SetGPDFillBuffer(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_FILL_BUFFER
    fields = [
        ('sample','f',1)
    ]

class SetGPDIntScale(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_SET_BUFFER_INT_SCALE
    fields = [
        ('scale','f',1)
    ]

class SetGPDFillBufferINT8(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_FILL_BUFFER_INT8
    fields = [
        ('sample','i',1)
    ]

class SetGPDFillBufferINT16(metaclass=VESCMessage):
    id = VedderCmd.COMM_GPD_FILL_BUFFER_INT16
    fields = [
        ('sample','b',1)
    ]

class SetDutyCycle(metaclass=VESCMessage):
    """ Set the duty cycle.

    :ivar duty_cycle: Value of duty cycle to be set (range [-1e5, 1e5]).
    """
    id = VedderCmd.COMM_SET_DUTY
    fields = [
        ('duty_cycle', 'i', 100000)
    ]


class SetRPM(metaclass=VESCMessage):
    """ Set the RPM.

    :ivar rpm: Value to set the RPM to.
    """
    id = VedderCmd.COMM_SET_RPM
    fields = [
        ('rpm', 'i')
    ]


class SetCurrent(metaclass=VESCMessage):
    """ Set the current (in milliamps) to the motor.

    :ivar current: Value to set the current to (in milliamps).
    """
    id = VedderCmd.COMM_SET_CURRENT
    fields = [
        ('current', 'i', 1000)
    ]


class SetCurrentBrake(metaclass=VESCMessage):
    """ Set the current brake (in milliamps).

    :ivar current_brake: Value to set the current brake to (in milliamps).
    """
    id = VedderCmd.COMM_SET_CURRENT_BRAKE
    fields = [
        ('current_brake', 'i', 1000)
    ]


class SetPosition(metaclass=VESCMessage):
    """Set the rotor angle based off of an encoder or sensor
    
    :ivar pos: Value to set the current position or angle to.
    """
    id = VedderCmd.COMM_SET_POS
    fields = [
        ('pos', 'i', 1000000)
    ]


class SetRotorPositionMode(metaclass=VESCMessage):
     """Sets the rotor position feedback mode.

     It is reccomended to use the defined modes as below:
         * DISP_POS_OFF
         * DISP_POS_MODE_ENCODER
         * DISP_POS_MODE_PID_POS
         * DISP_POS_MODE_PID_POS_ERROR

     :ivar pos_mode: Value of the mode
     """

     DISP_POS_OFF = 0
     DISP_POS_MODE_ENCODER = 3
     DISP_POS_MODE_PID_POS = 4
     DISP_POS_MODE_PID_POS_ERROR = 5

     id = VedderCmd.COMM_SET_DETECT
     fields = [
         ('pos_mode', 'b')
     ]


class SetServoPosition(metaclass=VESCMessage):
    """Sets the position of s servo connected to the VESC.

    :ivar servo_pos: Value of position (range [0, 1])
    """

    id = VedderCmd.COMM_SET_SERVO_POS
    fields = [
        ('servo_pos', 'h', 1000)
    ]

class Alive(metaclass=VESCMessage):
    """Heartbeat signal to keep VESC alive"""
    id = VedderCmd.COMM_ALIVE
    fields = []


# statically save this message because it does not need to be recalculated
alive_msg = encode(Alive())
