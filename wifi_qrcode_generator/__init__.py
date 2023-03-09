"""Command line utility and API to generate a QR code for your WiFi network to let others quickly 
connect.
"""

from wifi_qrcode_generator import runner, generator
from wifi_qrcode_generator.generator import *

__all__ = generator.__all__


if __name__ == '__main__':
    runner.main()
