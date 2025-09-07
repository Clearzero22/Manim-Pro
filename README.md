# Manim Binary Tree Construction Animation

This project demonstrates how to construct a binary tree from inorder and postorder traversal arrays using Manim, a powerful mathematical animation engine.

## Overview

The project contains two implementations of binary tree construction animations:

1. `main.py` - A basic implementation showing the construction of a binary tree with hardcoded values
2. `tree.py` - An advanced implementation that visualizes the recursive process of building a binary tree from traversal arrays

The animation visualizes the algorithm for constructing a binary tree using inorder and postorder traversal arrays:
- Inorder: [9, 3, 15, 20, 7]
- Postorder: [9, 15, 7, 20, 3]

## Features

- Visual representation of binary tree construction process
- Step-by-step animation of recursive calls
- Highlighting of array ranges during recursion
- Visualization of the call stack during tree construction
- Custom tree node design with circular nodes and text labels

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) - Python package and project manager

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Clearzero22/Manim-Pro.git
   cd Manim-Pro
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

### Running the Basic Animation

To run the basic binary tree construction animation:

```bash
uv run manim -pql main.py BuildTreeAnimation
```

### Running the Advanced Animation

To run the advanced animation that shows the recursive process:

```bash
uv run manim -pql tree.py BuildTreeAnimation
```

### Command Line Options

- `-p`: Preview the animation in a popup window
- `-q`: Quality setting (l=low, m=medium, h=high, p=production)
- `-l`: Low quality (faster rendering, useful for development)

### Output

The generated videos will be saved in the `media/videos/` directory.

## Project Structure

```
.
├── main.py              # Basic binary tree animation
├── tree.py              # Advanced recursive tree construction animation
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # uv lock file
├── .python-version     # Python version specification
├── .gitignore          # Git ignore configuration
├── README.md           # This file
├── dev_doc/            # Development documentation
│   ├── 1. use_guide.md # Usage guide (Chinese)
│   └── 2. development_guide.md # Development guide (Chinese)
└── media/              # Media files (videos, images)
    ├── images/
    ├── texts/
    └── videos/
```

## Development

For development instructions, please refer to the [Development Guide](dev_doc/2.%20development_guide.md) (in Chinese).

## How It Works

The algorithm works by:

1. Taking the last element of the postorder array as the root
2. Finding the root's position in the inorder array
3. Recursively building the left and right subtrees
4. The left subtree consists of elements before the root in inorder
5. The right subtree consists of elements after the root in inorder

The animation visualizes this process by:
- Displaying the input arrays
- Highlighting the current working range in both arrays
- Showing the recursive call stack
- Animating the construction of nodes and edges

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Manim Community](https://www.manim.community/) for the amazing mathematical animation engine
- [uv](https://github.com/astral-sh/uv) for the ultra-fast Python package installer and resolver