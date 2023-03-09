from typing import Tuple, Literal, overload
import qrcode

__all__: Tuple[str, ...]

AUTHENTICATION_TYPES: Tuple[Literal['WPA'], Literal['WEP'], Literal['nopass']]

@overload
def wifi_code(ssid: str, hidden: bool, authentication_type: Literal['nopass'],
              password: Literal[None] = None) -> str: ...
@overload
def wifi_code(ssid: str, hidden: bool, authentication_type: Literal['WPA', 'WEP'],
              password: str) -> str: ...

@overload
def wifi_qrcode(ssid: str, hidden: bool, authentication_type: Literal['nopass'],
                password: Literal[None] = None, **kwargs) -> qrcode.QRCode: ...
@overload
def wifi_qrcode(ssid: str, hidden: bool, authentication_type: Literal['WPA', 'WEP'],
                password: str, **kwargs) -> qrcode.QRCode: ...
