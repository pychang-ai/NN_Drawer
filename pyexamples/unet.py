import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define the architecture
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    # Encoder Path (Contracting)
    
    # Input
    to_Conv("conv1_1", 64, 32, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=2),
    to_Conv("conv1_2", 64, 32, offset="(2,0,0)", to="(conv1_1-east)", height=32, depth=32, width=2),
    to_Pool("pool1", offset="(2,0,0)", to="(conv1_2-east)", height=28, depth=28, width=1),
    
    # Level 2
    to_Conv("conv2_1", 128, 16, offset="(2,0,0)", to="(pool1-east)", height=28, depth=28, width=2),
    to_Conv("conv2_2", 128, 16, offset="(2,0,0)", to="(conv2_1-east)", height=28, depth=28, width=2),
    to_Pool("pool2", offset="(2,0,0)", to="(conv2_2-east)", height=24, depth=24, width=1),
    
    # Level 3
    to_Conv("conv3_1", 256, 8, offset="(2,0,0)", to="(pool2-east)", height=24, depth=24, width=2),
    to_Conv("conv3_2", 256, 8, offset="(2,0,0)", to="(conv3_1-east)", height=24, depth=24, width=2),
    to_Pool("pool3", offset="(2,0,0)", to="(conv3_2-east)", height=20, depth=20, width=1),
    
    # Level 4 (Bottom)
    to_Conv("conv4_1", 512, 4, offset="(2,0,0)", to="(pool3-east)", height=20, depth=20, width=2),
    to_Conv("conv4_2", 512, 4, offset="(2,0,0)", to="(conv4_1-east)", height=20, depth=20, width=2),
    
    # Decoder Path (Expanding)
    
    # Level 3
    to_UnPool("unpool3", offset="(2,0,0)", to="(conv4_2-east)", height=24, depth=24, width=1),
    to_Conv("up_conv3_1", 256, 8, offset="(2,0,0)", to="(unpool3-east)", height=24, depth=24, width=2),
    to_Conv("up_conv3_2", 256, 8, offset="(2,0,0)", to="(up_conv3_1-east)", height=24, depth=24, width=2),
    
    # Level 2
    to_UnPool("unpool2", offset="(2,0,0)", to="(up_conv3_2-east)", height=28, depth=28, width=1),
    to_Conv("up_conv2_1", 128, 16, offset="(2,0,0)", to="(unpool2-east)", height=28, depth=28, width=2),
    to_Conv("up_conv2_2", 128, 16, offset="(2,0,0)", to="(up_conv2_1-east)", height=28, depth=28, width=2),
    
    # Level 1
    to_UnPool("unpool1", offset="(2,0,0)", to="(up_conv2_2-east)", height=32, depth=32, width=1),
    to_Conv("up_conv1_1", 64, 32, offset="(2,0,0)", to="(unpool1-east)", height=32, depth=32, width=2),
    to_Conv("up_conv1_2", 64, 32, offset="(2,0,0)", to="(up_conv1_1-east)", height=32, depth=32, width=2),
    
    # Output
    to_Conv("output", 2, 32, offset="(2,0,0)", to="(up_conv1_2-east)", height=32, depth=32, width=1, caption="Output"),
    
    # Connections
    to_connection("conv1_1", "conv1_2"),
    to_connection("conv1_2", "pool1"),
    to_connection("pool1", "conv2_1"),
    to_connection("conv2_1", "conv2_2"),
    to_connection("conv2_2", "pool2"),
    to_connection("pool2", "conv3_1"),
    to_connection("conv3_1", "conv3_2"),
    to_connection("conv3_2", "pool3"),
    to_connection("pool3", "conv4_1"),
    to_connection("conv4_1", "conv4_2"),
    to_connection("conv4_2", "unpool3"),
    to_connection("unpool3", "up_conv3_1"),
    to_connection("up_conv3_1", "up_conv3_2"),
    to_connection("up_conv3_2", "unpool2"),
    to_connection("unpool2", "up_conv2_1"),
    to_connection("up_conv2_1", "up_conv2_2"),
    to_connection("up_conv2_2", "unpool1"),
    to_connection("unpool1", "up_conv1_1"),
    to_connection("up_conv1_1", "up_conv1_2"),
    to_connection("up_conv1_2", "output"),
    
    # Skip Connections
    to_skip("conv1_2", "up_conv1_1"),
    to_skip("conv2_2", "up_conv2_1"),
    to_skip("conv3_2", "up_conv3_1"),
    
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
