# Kivy Headless Renderer for Raspberry Pi

This project demonstrates the use of the Kivy framework to create a headless renderer for a Raspberry Pi. The renderer is specifically designed for and tested with the ST7789 SPI display, but it should work with other SPI displays as well. The code utilizes the Adafruit RGB Display library to communicate with the display. The renderer is optimized to not update the LCD if nothing has changed in the frame.

## Requirements

- Raspberry Pi 4
- SPI Display (tested with ST7789 module)
- [Poetry](https://python-poetry.org/)

## Dependencies

You need to compile and install SDL2 from source with `kmsdrm` backend. Please follow the instructions provided [here](https://kivy.org/doc/stable/installation/installation-rpi.html#raspberry-pi-4-headless-installation-on-raspbian-buster)

### Poetry

To install poetry in Raspbian you need to follow these instructions until [this issue](https://github.com/python-poetry/poetry/issues/7645) is resolved:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh # Select "2) Customize installation" and set host to "arm-unknown-linux-gnueabihf"
sudo apt-get install pkg-config libssl-dev
curl -sSL https://install.python-poetry.org | python3 -
```

After having poetry, to install the required dependencies, run the following command:

```sh
poetry install --with rpi
```

### Pip

Since installing poetry on Raspberry Pi 4 is a bit tricky at the moment, you may consider this alternative:

1 Create a virtualenv manually
1 Run:

```sh
      pip install requirements.txt
```

`requirements.txt` is provided and kept up to date until the above mentioned issue is resolved.

## Usage

1. Call setup_headless() before inheriting the `HeadlessWidget` class for the root widget of your application, and provide the optional parameters as needed. For example:

   ```python
   setup_headless(
       min_fps=1,
       max_fps=20,
       width=240,
       height=240,
       baudrate=96000000,
       debug_mode=False,
       display_class=ST7789,
       double_buffering=True,
       synchronous_clock=True,
   )
   ```

1. Inherit the `HeadlessWidget` class for the root widget of your Kivy application. For example:

   ```python
   class FboFloatLayout(FloatLayout, HeadlessWidget):
       pass
   ```

1. Run the Kivy app as you normally would.

Checkout [demo.py](./src/demo/demo.py) to see a sample implementation.

## Parameters

These parameters can be set to control the behavior of headless kivy pi:

### `min_fps`

Minimum frames per second for when the Kivy application is idle.

### `max_fps`

Maximum frames per second for the Kivy application.

### `width`

The width of the display in pixels.

### `height`

The height of the display in pixels.

### `baudrate`

The baud rate for the display connection.

### `debug_mode`

If set to True, the application will print debug information, including FPS.

### `display_class`

The display class to use (default is ST7789).

### `double_buffering`

Is set to `True`, it will let Kivy generate the next frame while sending the last frame to the display.

### `synchronous_clock`

If set to True, Kivy will wait for the LCD before rendering next frames. This will cause Headless to skip frames if they are rendered before the LCD has finished displaying the previous frames. If set to False, frames will be rendered asynchronously, letting Kivy render frames regardless of display being able to catch up or not at the expense of possible frame skipping.

## Important Note

This project has only been tested with the ST7789 SPI display module. Other display modules might not be compatible or may require changing the parameters or even modifications to the code.

## License

This project is released under the MIT License.
