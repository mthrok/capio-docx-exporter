import logging
import argparse

from .api_client import fetch_transcript

_LG = logging.getLogger(__name__)


def _parse_command_line_args():

    parser = argparse.ArgumentParser(
        description='Fetch transcription result and save it in docx format'
    )
    parser.add_argument(
        '--id', help='Transcript ID', default='593f237fbcae700012ba8fcd'
    )
    parser.add_argument(
        '--key', help='API KEY', default='262ac9a0c9ba4d179aad4c0b9b02120a',
    )
    parser.add_argument(
        '--debug', help='Enable debug log', action='store_true',
    )
    return parser.parse_args()


def _init_logging(debug):
    message_format = (
        '%(asctime)s: %(levelname)5s: %(funcName)10s: %(message)s'
        if debug else '%(asctime)s: %(levelname)5s: %(message)s'
    )
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format=message_format, level=level)


def main():
    """Main entrypoint for `capio_word_exporter` command.

    Currently generate word file from transcription result.
    """
    args = _parse_command_line_args()
    _init_logging(args.debug)
    data = fetch_transcript(args.id, args.key)
    _LG.info(data)


if __name__ == '__main__':
    main()
