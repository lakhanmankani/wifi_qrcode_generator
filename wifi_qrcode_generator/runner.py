"""Command line utility to generate a WiFI QR code."""

import argparse
import getpass
import sys

from wifi_qrcode_generator import generator, __version__


parser = argparse.ArgumentParser()
parser.add_argument('-V', '--version', action='store_true',
                    help='Show the version number')

# Non-interactive flags
parser.add_argument('-s', '--ssid', help='network SSID', type=str)
parser.add_argument('-p', '--password', help='network password', type=str)
parser.add_argument(
    '-H', '--hidden', help='network is hidden', type=bool, default=False)
parser.add_argument('-a', '--auth-type', help='authentication type',
                    choices=generator.AUTHENTICATION_TYPES, type=str, default='WPA')
parser.add_argument(
    '-o', '--output', help='save QR code as PNG to output path', type=str)
parser.add_argument('-P', '--print-ascii',
                    help='print ASCII QR code', action='store_true')


def non_interactive(args: argparse.Namespace):
    """Run app in non-interactive mode.

    Args:
        args: The parsed arguments.
    """
    if args.output is None and not args.print_ascii:
        print('Either -o or -P or both flags must be passed!')
        return
    qr_code = generator.wifi_qrcode(
        args.ssid, args.hidden, args.auth_type, args.password)

    if args.output != '':
        qr_code.make_image().save(f'{args.output}')
    if args.print_ascii:
        qr_code.print_ascii()


def interactive():
    """Run app in interactive mode."""
    ssid = input('SSID: ')
    if ssid == '':
        print('Input is not valid!')
        return

    hidden_input = input('Is the network hidden [y/N]: ').lower().strip()
    if hidden_input in ['yes', 'y', 'true', 't']:
        hidden = True
    elif hidden_input in ['', 'no', 'n', 'false', 'f']:
        hidden = False
    else:
        print('Input is not valid!')
        return

    print('Authentication types:')
    for i, auth_type in enumerate(generator.AUTHENTICATION_TYPES):
        print(f'- [{i+1}] {auth_type}')
    authentication_type_i = input(
        f'Select authentication type [1-{len(generator.AUTHENTICATION_TYPES)}]: ')
    try:
        auth_type = generator.AUTHENTICATION_TYPES[int(
            authentication_type_i)-1]
    except (ValueError, IndexError):
        print('Input is not valid!')
        return

    if auth_type == 'nopass':
        password = None
    else:
        password = getpass.getpass('Password: ')
        if password == '':
            print('Input is not valid!')
            return
    qr_code = generator.wifi_qrcode(
        ssid, hidden, auth_type, password)

    save_qr_code = input('Save QR code [Y/n]: ').lower().strip()
    if save_qr_code in ['', 'yes', 'y', 'true', 't']:
        qr_code.make_image().save(f'{ssid}.png')
        print(
            f'The QR code has been stored in the current directory as {ssid}.png')
    elif save_qr_code not in ['no', 'n', 'false', 'f']:
        print('Input is not valid!')
        return

    display_qr_code = input('Display QR code [y/N]: ').lower().strip()
    if display_qr_code in ['yes', 'y', 'true', 't']:
        qr_code.print_ascii()
    elif display_qr_code not in ['', 'no', 'n', 'false', 'f']:
        print('Input is not valid!')
        return


def version():
    """Display current version."""
    print(f'WiFi QR code generator V{__version__.__version__}')


def main():
    """Entry point for app."""
    args = parser.parse_args()
    if args.version:
        version()
    elif len(sys.argv) > 1:
        # Argument other than version passed, use non-interactive mode
        non_interactive(args)
    else:
        # No arguments passed, use interactive mode
        interactive()


if __name__ == '__main__':
    main()
