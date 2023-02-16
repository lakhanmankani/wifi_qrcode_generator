"""Command line utility and API to generate a QR code for your WiFi network to let others quickly 
connect.
"""

from wifi_qrcode_generator import runner
from wifi_qrcode_generator.generator import *


if __name__ == '__main__':
    runner.main()
