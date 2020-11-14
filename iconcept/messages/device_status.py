from iconcept.message_extractor import extract_datagram


class DeviceStatus:
    HEADER_PATTERN = '550901'
    HEADER_LENGTH = 6
    MESSAGE_LENGTH = 2

    def __init__(self, message: str):
        self.message = extract_datagram(message, self.HEADER_PATTERN, self.HEADER_LENGTH + self.MESSAGE_LENGTH)

    def is_valid(self) -> bool:
        return self.message is not None

    def get_status(self) -> int:
        if not self.is_valid():
            return 0

        status_hex = self.message[6: 6 + 2]
        return int(status_hex, 16)
