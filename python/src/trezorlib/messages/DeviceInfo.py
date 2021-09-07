# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DeviceInfo(p.MessageType):
    MESSAGE_WIRE_TYPE = 10003

    def __init__(
        self,
        *,
        serial_no: str = None,
        spiFlash_info: str = None,
        SE_info: str = None,
        NFT_voucher: bytes = None,
        cpu_info: str = None,
        pre_firmware: str = None,
    ) -> None:
        self.serial_no = serial_no
        self.spiFlash_info = spiFlash_info
        self.SE_info = SE_info
        self.NFT_voucher = NFT_voucher
        self.cpu_info = cpu_info
        self.pre_firmware = pre_firmware

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('serial_no', p.UnicodeType, None),
            2: ('spiFlash_info', p.UnicodeType, None),
            3: ('SE_info', p.UnicodeType, None),
            4: ('NFT_voucher', p.BytesType, None),
            5: ('cpu_info', p.UnicodeType, None),
            6: ('pre_firmware', p.UnicodeType, None),
        }