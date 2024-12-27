import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define the architecture
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    # First Conv Block
    to_Conv("conv1_1", 64, 32, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=2),
    to_Conv("conv1_2", 64, 32, offset="(2,0,0)", to="(conv1_1-east)", height=32, depth=32, width=2),
    to_Pool("pool1", offset="(2,0,0)", to="(conv1_2-east)", height=28, depth=28, width=1),
    
    # Second Conv Block
    to_Conv("conv2_1", 128, 16, offset="(2,0,0)", to="(pool1-east)", height=25, depth=25, width=2),
    to_Conv("conv2_2", 128, 16, offset="(2,0,0)", to="(conv2_1-east)", height=25, depth=25, width=2),
    to_Pool("pool2", offset="(2,0,0)", to="(conv2_2-east)", height=21, depth=21, width=1),
    
    # Dense layers
    to_SoftMax("flatten", 1024, "(2,0,0)", "(pool2-east)", caption="Flatten"),
    to_SoftMax("dense1", 512, "(2,0,0)", "(flatten-east)", caption="Dense"),
    to_SoftMax("dense2", 10, "(2,0,0)", "(dense1-east)", caption="Output"),
    
    # Connections
    to_connection("conv1_1", "conv1_2"),
    to_connection("conv1_2", "pool1"),
    to_connection("pool1", "conv2_1"),
    to_connection("conv2_1", "conv2_2"),
    to_connection("conv2_2", "pool2"),
    to_connection("pool2", "flatten"),
    to_connection("flatten", "dense1"),
    to_connection("dense1", "dense2"),
    
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
