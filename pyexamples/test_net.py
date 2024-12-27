import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define the architecture
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    # Input layer
    to_input('input.dat'),
    
    # Convolution layers
    to_Conv("conv1", 64, "28,28,1", offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=2),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    
    # Second convolution layer
    to_Conv("conv2", 128, "14,14,64", offset="(2,0,0)", to="(pool1-east)", height=28, depth=28, width=2),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)"),
    
    # Dense layers
    to_Dense("dense1", 256, offset="(2,0,0)", to="(pool2-east)", height=8, depth=20, width=2),
    to_Dense("dense2", 10, offset="(2,0,0)", to="(dense1-east)", height=4, depth=12, width=2),
    
    # Connect layers
    to_connection("pool1", "conv2"),
    to_connection("pool2", "dense1"),
    to_connection("dense1", "dense2"),
    
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')
