"""VGG

Adapted from https://github.com/pytorch/vision/torchvision/models/ 'vgg.py' (BSD-3-Clause)
with a few changes for a custom functionality.

"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# VGG 13
VGG = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M']
# Dense layears are 4096 -> 4096 -> 1000 (in our case 3)

class VGG(nn.Module):
    def __init__(self, ):
        self.a = None
