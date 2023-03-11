"""Generate WiFi QR code."""

import qrcode

__all__ = 'wifi_code', 'wifi_qrcode', 'AUTHENTICATION_TYPES'

AUTHENTICATION_TYPES = ('WPA', 'WEP', 'nopass')


def wifi_code(ssid, hidden, authentication_type, password=None) -> str:
    """Generate a WiFi code for the given parameters. 

    The generated WiFi code can be rendered into a QR code to be scanned to join the network.

    Args:
        ssid: Network SSID.
        hidden: Specify if the network is hidden.
        authentication_type: Specify the authentication type. Supported types: 
          `WPA`, `WEP`, `nopass`. 
        password: Network password. If `authetication_type` is `None`, this argument should be set
          to `None`.
    Returns:
        The WiFi code for the given parameters.
    """
    hidden = 'true' if hidden else 'false'

    if authentication_type in ['WPA', 'WEP']:
        if password is None:
            raise TypeError('For WPA and WEP, password should not be None.')
        return f'WIFI:T:{authentication_type};S:{ssid};P:{password};H:{hidden};;'
    if authentication_type == 'nopass':
        if password is not None:
            raise TypeError('For nopass, password should be None.')
        return f'WIFI:T:nopass;S:{ssid};H:{hidden};;'
    raise ValueError(f'Unknown authentication_type: {authentication_type}')


def wifi_qrcode(ssid, hidden, authentication_type, password=None, **kwargs) -> qrcode.QRCode:
    """Generate WiFi QR code for given parameters.

    The generated QR code can be scanned to join the network. 
    This function is a wrapper of `wifi_code` that generates a QR from it's output.

    Args:
        ssid: Network SSID.
        hidden: Specify if the network is hidden.
        authentication_type: Specify the authentication type. Supported types: 
          `WPA`, `WEP`, `nopass`. 
        password: Network password. If `authetication_type` is `None`, this argument should be set
          to `None`.
        **kwargs: Optional keyword arguments to use with `qrcode.QRCode`. See the arguments for 
          `qrcode.QRCode`.

    Returns:
        A QR code for the given parameters.
    """
    code = wifi_code(ssid, hidden, authentication_type, password)
    qr_code = qrcode.QRCode(**kwargs)
    qr_code.add_data(code)
    return qr_code
