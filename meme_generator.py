from PIL import Image, ImageDraw, ImageFont
import textwrap

def make_meme(image_path, top_text, bottom_text, output_path, font_path=None, font_size=40):
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size

    # Load a font
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)

    # Function to draw text (top or bottom)
    def draw_text(text, position):
        # Wrap text to fit image width
        char_width, char_height = font.getsize("A")
        max_chars = image_width // char_width
        lines = textwrap.wrap(text, width=max_chars)
        y_text = position
        for line in lines:
            line_width, line_height = font.getsize(line)
            x_text = (image_width - line_width) / 2
            # Add outline
            for dx in [-2, 0, 2]:
                for dy in [-2, 0, 2]:
                    if dx != 0 or dy != 0:
                        draw.text((x_text + dx, y_text + dy), line, font=font, fill='black')
            draw.text((x_text, y_text), line, font=font, fill='white')
            y_text += line_height

    # Draw top text
    draw_text(top_text, 10)
    # Draw bottom text
    # Estimate height of bottom text
    char_width, char_height = font.getsize("A")
    max_chars = image_width // char_width
    lines = textwrap.wrap(bottom_text, width=max_chars)
    total_height = len(lines) * char_height
    draw_text(bottom_text, image_height - total_height - 10)

    # Save the meme
    img.save(output_path)

if __name__ == "__main__":
    # Example usage
    make_meme(
        image_path="sample.jpg",            # Path to your image
        top_text="Top Meme Text",           # Top text
        bottom_text="Bottom Meme Text",     # Bottom text
        output_path="meme_output.jpg",      # Output file
        font_path=None,                     # Or specify a .ttf file
        font_size=40                        # Font size
    )
