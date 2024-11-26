# Pixel Art 🎨

Pixel Art is a Python package that allows you to create, customize, and display pixel art directly in your terminal. Whether you're a hobbyist exploring creative coding or a retro game designer, this package provides intuitive tools to bring your designs to life.

## 🌟 Features

- **Pre-Made Examples:** Jumpstart your projects with ready-to-use pixel art templates.
- **Custom Pixel Art:** Design your own pixel masterpieces with ease.
- **Terminal-Friendly:** Render pixel art directly in your terminal for quick previews.
- **Lightweight & Fast:** Optimized for performance and simplicity.

## 🚀 Installation

### From Source:

1. Clone the repository:

```bash
git clone https://github.com/mahmoudnasser1561/pixel-art.git
```

2 .Navigate to the project directory:

```bash
cd pixel_art
```

3- Install the package:

```
pip install .
```

## 🛠️ Usage
## Quick Start 🚀

### Display a Pre-Made Example

```python
from pixel_art.examples import examples

# Display the pre-made house example
examples.show_house()
```
```
   🟥🟥🟥   
  🟥🟩🟩🟥  
 🟥🟩🟩🟩🟥 
🟫🟫🟫🟫🟫🟫
```



### Create Your Own Pixel Art

```python
from pixel_art.pixels import PixelArt

# Create a blank 10x10 canvas
art = PixelArt(width=10, height=10)

# Set some pixels
art.set_pixel(4, 4, "🔴")  # Red circle at (4, 4)
art.set_pixel(5, 5, "🟢")  # Green circle at (5, 5)

# Display the art
art.display()
```

### create a smile face
```python
import pixel_art

smile = pixel_art.pixels.Image()
smile.add_row(0, 'yellow')
smile.add_row(1, 'yellow', 'yellow', 'black', 'yellow', 'black', 'yellow', 'yellow')
smile.add_row(2, 'yellow', 'yellow', 'black', 'yellow', 'black', 'yellow', 'yellow')
smile.add_row(3, 'yellow')
smile.add_row(4, 'yellow', 'black', 'yellow', 'yellow', 'yellow', 'black', 'yellow')
smile.add_row(5, 'yellow', 'yellow', 'black', 'black', 'black', 'yellow', 'yellow')
smile.add_row(6, 'yellow')
smile.display()
```
![smile face](https://github.com/mahmoudnasser1561/pixel_art/blob/main/media_1_6763095104801fc879d120bf46dcbe32-f7e22cc25e0ad845.webp)


## 📁 Project Structure

```bash
pixel_art/
├── pixel_art/
│   ├── __init__.py       # Package initialization
│   ├── pixels.py         # Core pixel art creation and rendering logic
│   ├── examples.py       # Pre-made pixel art examples
├── setup.py              # Package metadata and dependencies
└── README.md             # User guide (this file)
```
