#!/usr/bin/env python3

import argparse
from core import disconnect, BluezTarget, BluezAddressType


def main():
    parser = argparse.ArgumentParser(
        prog="Disconnect",
        description="Try to disconnect a device using system tools",
    )
    parser.add_argument(
        "-a",
        "--target-address",
        help="Target device MAC address",
        required=True,
        dest="address",
    )
    parser.add_argument(
        "-t",
        "--target-address-type",
        help="Target device MAC address type",
        dest="address_type",
        type=lambda t: BluezAddressType[t],
        choices=list(BluezAddressType),
        default=BluezAddressType.BR_EDR,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="activate verbose mode",
        dest="verboseMode",
        action = "store_true",
    )
    args = parser.parse_args()

    disconnect(BluezTarget(args.address, args.address_type), verbose=args.verboseMode)


if __name__ == "__main__":
    main()
