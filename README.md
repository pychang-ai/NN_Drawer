# Neural Network Architecture Visualization

This repository contains tools and examples for visualizing neural network architectures using TikZ and LaTeX. It provides a clean and professional way to create publication-quality neural network architecture diagrams.

## Features

- Beautiful and customizable neural network architecture visualization
- Support for various layer types (Conv, Pool, FC, etc.)
- Easy-to-use Python interface for generating diagrams
- Multiple example architectures included

## Examples

The repository includes visualizations for several popular neural network architectures:

- PSPNet (Pyramid Scene Parsing Network)
- U-Net
- DeepLabV3+
- Custom CNN architectures

## Requirements

- Python 3.x
- LaTeX distribution (e.g., MiKTeX or TeX Live)
- Required Python packages:
  - graphviz
  - python-graphviz
  - numpy
  - matplotlib

## Usage

1. Clone the repository:
```bash
git clone https://github.com/pychang-ai/NN_Drawer.git
cd NN_Drawer/PlotNeuralNet
```

2. Check the examples in the `pyexamples` directory:
```bash
cd pyexamples
python pspnet.py  # Generates PSPNet architecture
python unet.py    # Generates U-Net architecture
```

3. Create your own architecture:
- Copy one of the example files
- Modify the network structure according to your needs
- Run the Python script to generate the diagram

## Directory Structure

- `layers/`: Contains LaTeX style files and basic building blocks
- `pycore/`: Core Python utilities for generating network diagrams
- `pyexamples/`: Example network architecture implementations
  - `pspnet.py`: PSPNet implementation
  - `unet.py`: U-Net implementation
  - `deeplabv3plus.py`: DeepLabV3+ implementation
  - `custom_cnn.py`: Custom CNN example

## Contributing

Feel free to contribute by:
1. Opening issues for bugs or feature requests
2. Submitting pull requests for improvements
3. Adding new network architecture examples

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project is based on the PlotNeuralNet framework and has been enhanced with additional features and examples.

## Getting Started
1. Install the following packages on Ubuntu.
    * Ubuntu 16.04
        ```
        sudo apt-get install texlive-latex-extra
        ```

    * Ubuntu 18.04.2
Base on this [website](https://gist.github.com/rain1024/98dd4e2c6c8c28f9ea9d), please install the following packages.
        ```
        sudo apt-get install texlive-latex-base
        sudo apt-get install texlive-fonts-recommended
        sudo apt-get install texlive-fonts-extra
        sudo apt-get install texlive-latex-extra
        ```

    * Windows
    1. Download and install [MikTeX](https://miktex.org/download).
    2. Download and install bash runner on Windows, recommends [Git bash](https://git-scm.com/download/win) or Cygwin(https://www.cygwin.com/)

2. Execute the example as followed.
    ```
    cd pyexamples/
    bash ../tikzmake.sh test_simple
    ```

## TODO

- [X] Python interface
- [ ] Add easy legend functionality
- [ ] Add more layer shapes like TruncatedPyramid, 2DSheet etc
- [ ] Add examples for RNN and likes.

## Latex usage

See [`examples`](examples) directory for usage.

## Python usage

First, create a new directory and a new Python file:

    $ mkdir my_project
    $ cd my_project
    vim my_arch.py

Add the following code to your new file:

```python
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    to_connection( "pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    to_connection("pool2", "soft1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
```

Now, run the program as follows:

    bash ../tikzmake.sh my_arch

