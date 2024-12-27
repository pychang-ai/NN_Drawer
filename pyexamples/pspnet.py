import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define the architecture
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    # ResNet Backbone
    to_Conv("conv1", 64, 128, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2, caption="Conv1"),
    to_Pool("pool1", offset="(2,0,0)", to="(conv1-east)", height=32, depth=32, width=1),
    
    # ResNet Block 1
    to_Conv("res1_1", 256, 32, offset="(2,0,0)", to="(pool1-east)", height=32, depth=32, width=2),
    to_Conv("res1_2", 256, 32, offset="(2,0,0)", to="(res1_1-east)", height=32, depth=32, width=2),
    
    # ResNet Block 2
    to_Conv("res2_1", 512, 16, offset="(2,0,0)", to="(res1_2-east)", height=16, depth=16, width=2),
    to_Conv("res2_2", 512, 16, offset="(2,0,0)", to="(res2_1-east)", height=16, depth=16, width=2),
    
    # ResNet Block 3
    to_Conv("res3_1", 1024, 8, offset="(2,0,0)", to="(res2_2-east)", height=8, depth=8, width=2),
    to_Conv("res3_2", 1024, 8, offset="(2,0,0)", to="(res3_1-east)", height=8, depth=8, width=2),
    
    # Pyramid Pooling Module
    # 1x1 branch
    to_Pool("pool_1x1", offset="(3,3,0)", to="(res3_2-east)", height=1, depth=1, width=1, caption="1x1 pool"),
    to_Conv("conv_1x1", 256, 8, offset="(2,0,0)", to="(pool_1x1-east)", height=8, depth=8, width=2),
    
    # 2x2 branch
    to_Pool("pool_2x2", offset="(3,1,0)", to="(res3_2-east)", height=2, depth=2, width=1, caption="2x2 pool"),
    to_Conv("conv_2x2", 256, 8, offset="(2,0,0)", to="(pool_2x2-east)", height=8, depth=8, width=2),
    
    # 3x3 branch
    to_Pool("pool_3x3", offset="(3,-1,0)", to="(res3_2-east)", height=3, depth=3, width=1, caption="3x3 pool"),
    to_Conv("conv_3x3", 256, 8, offset="(2,0,0)", to="(pool_3x3-east)", height=8, depth=8, width=2),
    
    # 6x6 branch
    to_Pool("pool_6x6", offset="(3,-3,0)", to="(res3_2-east)", height=6, depth=6, width=1, caption="6x6 pool"),
    to_Conv("conv_6x6", 256, 8, offset="(2,0,0)", to="(pool_6x6-east)", height=8, depth=8, width=2),
    
    # Concatenation
    to_Conv("concat", 1024, 8, offset="(4,0,0)", to="(res3_2-east)", height=8, depth=8, width=2, caption="Concat"),
    
    # Final convolution
    to_Conv("conv_final", 512, 8, offset="(2,0,0)", to="(concat-east)", height=8, depth=8, width=2),
    
    # Upsampling and Output
    to_UnPool("unpool", offset="(2,0,0)", to="(conv_final-east)", height=64, depth=64, width=1),
    to_Conv("output", 150, 64, offset="(2,0,0)", to="(unpool-east)", height=64, depth=64, width=1, caption="Output"),
    
    # Connections
    to_connection("conv1", "pool1"),
    to_connection("pool1", "res1_1"),
    to_connection("res1_1", "res1_2"),
    to_connection("res1_2", "res2_1"),
    to_connection("res2_1", "res2_2"),
    to_connection("res2_2", "res3_1"),
    to_connection("res3_1", "res3_2"),
    
    # Pyramid Module connections
    to_connection("res3_2", "pool_1x1"),
    to_connection("pool_1x1", "conv_1x1"),
    to_connection("res3_2", "pool_2x2"),
    to_connection("pool_2x2", "conv_2x2"),
    to_connection("res3_2", "pool_3x3"),
    to_connection("pool_3x3", "conv_3x3"),
    to_connection("res3_2", "pool_6x6"),
    to_connection("pool_6x6", "conv_6x6"),
    
    # Concatenation connections
    to_connection("conv_1x1", "concat"),
    to_connection("conv_2x2", "concat"),
    to_connection("conv_3x3", "concat"),
    to_connection("conv_6x6", "concat"),
    to_connection("res3_2", "concat"),
    
    # Final connections
    to_connection("concat", "conv_final"),
    to_connection("conv_final", "unpool"),
    to_connection("unpool", "output"),
    
    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
