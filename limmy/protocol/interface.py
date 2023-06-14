import limmy.protocol.base
import limmy.protocol.packet.codec


def decode(buffer):
    """
    Decodes the next valid VESC message in a buffer.

    :param buffer: The buffer to attempt to parse from.
    :type buffer: bytes

    :return: limmy message, number of bytes consumed in the buffer. If nothing
             was parsed returns (None, 0).
    :rtype: `tuple`: (limmy message, int)
    """
    msg_payload, consumed = limmy.protocol.packet.codec.unframe(buffer)
    if msg_payload:
        return limmy.protocol.base.VESCMessage.unpack(msg_payload), consumed
    else:
        return None, consumed


def encode(msg):
    """
    Encodes a limmy message to a packet. This packet is a valid VESC packet and
    can be sent to a VESC via your serial port.

    :param msg: Message to be encoded. All fields must be initialized.
    :type msg: limmy message

    :return: The packet.
    :rtype: bytes
    """
    msg_payload = limmy.protocol.base.VESCMessage.pack(msg)
    packet = limmy.protocol.packet.codec.frame(msg_payload)
    return packet


def encode_request(msg_cls):
    """
    Encodes a limmy message for requesting a getter message. This function
    should be called when you want to request a VESC to return a getter
    message.

    :param msg_cls: The message type which you are requesting.
    :type msg_cls: limmy.messages.getters.[requested getter]

    :return: The encoded limmy message which can be sent.
    :rtype: bytes
    """
    msg_payload = limmy.protocol.base.VESCMessage.pack(msg_cls, header_only=True)
    packet = limmy.protocol.packet.codec.frame(msg_payload)
    return packet
