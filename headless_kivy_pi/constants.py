"""Provide constants of the package."""

import os
from pathlib import Path

from str_to_bool import str_to_bool

# Check if the code is running on a Raspberry Pi
IS_RPI = Path('/etc/rpi-issue').exists()

# Constants for calculations
BYTES_PER_PIXEL = 2
BITS_PER_BYTE = 11

# Configure the headless mode for the Kivy application and initialize the display

MIN_FPS = int(os.environ.get('HEADLESS_KIVY_PI_MIN_FPS', '1'))
MAX_FPS = int(os.environ.get('HEADLESS_KIVY_PI_MAX_FPS', '32'))
WIDTH = int(os.environ.get('HEADLESS_KIVY_PI_WIDTH', '240'))
HEIGHT = int(os.environ.get('HEADLESS_KIVY_PI_HEIGHT', '240'))
BAUDRATE = int(os.environ.get('HEADLESS_KIVY_PI_BAUDRATE', '60000000'))
IS_DEBUG_MODE = (
    str_to_bool(
        os.environ.get('HEADLESS_KIVY_PI_DEBUG', 'False' if IS_RPI else 'True'),
    )
    == 1
)
DOUBLE_BUFFERING = (
    str_to_bool(
        os.environ.get('HEADLESS_KIVY_PI_DOUBLE_BUFFERING', 'True'),
    )
    == 1
)
SYNCHRONOUS_CLOCK = (
    str_to_bool(
        os.environ.get('HEADLESS_KIVY_PI_SYNCHRONOUS_CLOCK', 'False'),
    )
    == 1
)
AUTOMATIC_FPS = (
    str_to_bool(
        os.environ.get('HEADLESS_KIVY_PI_AUTOMATIC_FPS', 'True'),
    )
    == 1
)
CLEAR_AT_EXIT = (
    str_to_bool(os.environ.get('HEADLESS_KIVY_PI_CLEAR_AT_EXIT', 'False')) == 1
)
