# Meme Generator

A simple meme generator in Python using the Pillow (PIL) library. This tool overlays top and bottom text onto any image, making it easy to create classic memes.

## Features

- Add top and bottom text to images
- Automatic text wrapping to fit image width
- Text is outlined for visibility
- Customizable font and font size

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) (`pip install Pillow`)

## Usage

1. Place your image (e.g., `sample.jpg`) in the project directory.
2. Run the script:

```bash
python meme_generator.py
```

3. The generated meme will be saved as `meme_output.jpg`.

## Customization

- **Change image/text/output:** Edit the `make_meme` call in `meme_generator.py`.
- **Font:** Use a custom `.ttf` font by specifying the `font_path` parameter.
- **Font size:** Adjust the `font_size` parameter.

## Example

```python
make_meme(
    image_path="sample.jpg",
    top_text="When you use Python",
    bottom_text="And everything just works",
    output_path="meme_output.jpg",
    font_path=None,  # Or set to a .ttf file path
    font_size=40
)
```

## License

MIT
