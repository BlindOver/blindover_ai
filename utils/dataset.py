from glob import glob
from PIL import Image
from typing import *

import torch
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

"""
path : dataset/
├── images
│    ├─ class 1
│        ├─ img1.jpg
│        ├─ ...
│    ├─ class 2
│        ├─ img1.jpg
│        ├─ ...
│    ├─ class 3
│        ├─ img1.jpg
│        ├─ ...
│    ├─ class 4
│        ├─ img1.jpg
│        ├─ ...
│    ├─ ...
│        ├─ ...
│        ├─ ...
"""


# image padding to prevent distortion of image
class Padding(object):

    def __init__(self, fill: Tuple[int, int, int] = (0, 0, 0)):
        self.fill = fill

    def __call__(self, src):
        w, h = src.size

        if w == h:
            return src
        elif w > h:
            out = Image.new(src.mode, (w, w), self.fill)
            out.paste(src, (0, (w - h) // 2))
            return out
        else:
            out = Image.new(src.mode, (h, h), self.fill)
            out.paste(src, ((h - w) // 2, 0))
            return out


def load_dataloader(
    path: str,
    subset: str = 'train',
    num_workers: int=8,
    batch_size: int=32,
    shuffle: bool=True,
    drop_last: bool = True,):
    data_path = path + subset

    augmentation = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(degrees=(-20, 20)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    
    images = ImageFolder(data_path, transform=transform, target_transform=None)

    data_loader = DataLoader(
        images,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        drop_last=drop_last,
    )

    return data_loader