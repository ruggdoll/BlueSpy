import argparse
from core import record, BluezTarget


def main():
    parser = argparse.ArgumentParser(
        prog="Just record",
        description="Try to record sound from a bluetooth device using system tools",
    )
    parser.add_argument(
        "-a",
        "--target-address",
        help="Target device MAC address",
        required=True,
        dest="address",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="File to store recorded audio",
        dest="outfile",
        default="recording.wav",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="activate verbose mode",
        dest="verboseMode",
        action = "store_true",
    )
    args = parser.parse_args()

    record(BluezTarget(args.address), outfile=args.outfile, verbose=args.verboseMode)


if __name__ == "__main__":
    main()
