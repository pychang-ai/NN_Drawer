import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define the architecture
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    # Encoder - Modified ResNet
    to_Conv("conv1", 64, 128, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=2, caption="Conv1"),
    to_Pool("pool1", offset="(2,0,0)", to="(conv1-east)", height=28, depth=28, width=1),
    
    # ResNet Block 1
    to_Conv("res1_1", 256, 64, offset="(2,0,0)", to="(pool1-east)", height=28, depth=28, width=2),
    to_Conv("res1_2", 256, 64, offset="(2,0,0)", to="(res1_1-east)", height=28, depth=28, width=2),
    
    # ResNet Block 2 with Atrous Conv
    to_Conv("res2_1", 512, 32, offset="(2,0,0)", to="(res1_2-east)", height=24, depth=24, width=2, caption="Atrous Conv"),
    to_Conv("res2_2", 512, 32, offset="(2,0,0)", to="(res2_1-east)", height=24, depth=24, width=2),
    
    # ASPP Module
    to_Conv("aspp1", 256, 32, offset="(3,2,0)", to="(res2_2-east)", height=20, depth=20, width=2, caption="ASPP 1"),
    to_Conv("aspp2", 256, 32, offset="(3,0,0)", to="(res2_2-east)", height=20, depth=20, width=2, caption="ASPP 2"),
    to_Conv("aspp3", 256, 32, offset="(3,-2,0)", to="(res2_2-east)", height=20, depth=20, width=2, caption="ASPP 3"),
    
    # Global Average Pooling
    to_Pool("gap", offset="(3,4,0)", to="(res2_2-east)", height=16, depth=16, width=1, caption="Global Pool"),
    
    # Concat and Conv
    to_Conv("concat", 256, 32, offset="(2,0,0)", to="(aspp2-east)", height=24, depth=24, width=2, caption="Concat"),
    
    # Decoder
    to_UnPool("unpool1", offset="(2,0,0)", to="(concat-east)", height=48, depth=48, width=1),
    to_Conv("dec1", 256, 48, offset="(2,0,0)", to="(unpool1-east)", height=48, depth=48, width=2),
    
    # Low-level features
    to_Conv("low_level", 48, 128, offset="(0,4,0)", to="(conv1-east)", height=64, depth=64, width=2, caption="Low-level"),
    
    # Final layers
    to_Conv("final1", 256, 48, offset="(2,0,0)", to="(dec1-east)", height=48, depth=48, width=2),
    to_Conv("final2", 256, 48, offset="(2,0,0)", to="(final1-east)", height=48, depth=48, width=2),
    to_Conv("output", 21, 48, offset="(2,0,0)", to="(final2-east)", height=48, depth=48, width=1, caption="Output"),
    
    # Main path connections
    to_connection("conv1", "pool1"),
    to_connection("pool1", "res1_1"),
    to_connection("res1_1", "res1_2"),
    to_connection("res1_2", "res2_1"),
    to_connection("res2_1", "res2_2"),
    
    # ASPP connections
    to_connection("res2_2", "aspp1"),
    to_connection("res2_2", "aspp2"),
    to_connection("res2_2", "aspp3"),
    to_connection("res2_2", "gap"),
    
    # Decoder connections
    to_connection("aspp1", "concat"),
    to_connection("aspp2", "concat"),
    to_connection("aspp3", "concat"),
    to_connection("gap", "concat"),
    to_connection("concat", "unpool1"),
    to_connection("unpool1", "dec1"),
    to_connection("dec1", "final1"),
    to_connection("final1", "final2"),
    to_connection("final2", "output"),
    
    # Skip connection
    to_skip("conv1", "low_level"),
    to_skip("low_level", "dec1"),
    
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
