"""Generate a QR code to make it easy for other people to connect to the wifi
network.
"""

import qrcode
import getpass

def wifi_code(ssid, hidden, authentication_type, password=None):
    """Generate a wifi code for the given parameters
    
    :ssid str: SSID
    :hidden bool: Specify if the network is hidden
    :authentication_type str: Specify the authentication type. Supported types: WPA, WEP, nopass
    :password Optional[str]: Password. Not required if authentication type is nopass
    
    :return: The wifi code for the given parameters
    :rtype: str
    """
    hidden = 'true' if hidden else 'false'
    if authentication_type in ('WPA', 'WEP'):
        if password is None:
            raise TypeError('For WPA and WEP, password should not be None.')
        return 'WIFI:T:{type};S:{ssid};P:{password};H:{hidden};;'.format(
            type=authentication_type, ssid=ssid, password=password, hidden=hidden
        )
    elif authentication_type == 'nopass':
        if password is not None:
            raise TypeError('For nopass, password should be None.')
        return 'WIFI:T:nopass;S:{ssid};H:{hidden};;'.format(
            ssid=ssid, hidden=hidden
        )
    raise ValueError('Unknown authentication_type: {!r}'.format(authentication_type))

def wifi_qrcode(ssid, hidden, authentication_type, password=None, **kwargs):
    """Generate Wifi QR code for given parameters

    :ssid str: SSID
    :hidden bool: Specify if the network is hidden
    :authentication_type str: Specify the authentication type. Supported types: WPA, WEP, nopass
    :password Optional[str]: Password. Not required if authentication type is nopass
    :kwargs: Optional keyword arguments to use with `qrcode.make`. See the arguments for `qrcode.QRCode`.

    :return: An image of the qrcode for the given parameters
    :rtype: PIL.Image.Image
    """

    return qrcode.make(wifi_code(ssid, hidden, authentication_type, password), **kwargs).get_image()


def main():
    while True:
        ssid = input("SSID: ")
        if ssid == "":
            print("Input is not valid!")
        else:
            break

    while True:
        hidden = input("Is the network hidden (default is false): ").lower()
        if hidden in ['yes', 'y', 'true', 't']:
            hidden = True
            break
        elif hidden in ['', 'no', 'n', 'false', 'f']:
            hidden = False
            break
        else:
            print("Input is not valid!")
    
    while True:
        print("Authentication types: WPA/WPA2, WEP, nopass")
        authentication_type = input("Authentication type (default is "
                                    "WPA/WPA2): ").lower()
        if authentication_type in ['', 'wpa2', 'wpa', 'wpa/wpa2', 'wpa2/wpa']:
            authentication_type = 'WPA'
            break
        elif authentication_type == 'WEP' or authentication_type == 'nopass':
            break
        else:
            print("Input is not valid!")
    
    while True:
        if authentication_type == 'nopass':
            password = None
            break    
        password = getpass.getpass("Password: ")
        if password == "":
            print("Input not valid!")
        else:
            break
    qrcode = wifi_qrcode(ssid, hidden, authentication_type, password)
    qrcode.save(ssid+'.png')
    print("The qr code has been stored in the current directory.")

if __name__ == '__main__':
    main()
