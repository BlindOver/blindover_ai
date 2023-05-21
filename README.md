# Build Deep Learning Model for blind individuals  
- Models: [ShuffleNetV2](https://arxiv.org/abs/1807.11164), [MobileNetV3](https://arxiv.org/abs/1905.02244), [MNASNet](https://arxiv.org/abs/1807.11626), [EfficientNetV2](https://arxiv.org/abs/2104.00298)  

### Sample images  
- Coca Cola  

<div align='center'>
    <a href='./'>
        <img src = './images/cola_front.JPG' width=200>
    </a>
    <a href='./'>
        <img src = './images/cola_back.JPG' width=200>
    </a>
    <a href='./'>
        <img src = './images/cola_big.JPG' width=200>
    </a>
</div>

- Sprite Zero  

<div align='center'>
    <a href='./'>
        <img src = './images/sprite_zero_front.JPG' width=200>
    </a>
    <a href='./'>
        <img src = './images/sprite_zero_back.JPG' width=200>
    </a>
    <a href='./'>
        <img src = './images/sprite_zero.JPG' width=200>
    </a>
</div>


### Dataset Directory Guide
```
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
│    ├─ ...
│        ├─ ...
│        ├─ ...
```

### Training
```
python3 train.py --data_path '{dataset directory}' --name 'exp' --model '{the one of 4 models}' --pretrained --img_size 224 --num_workers 8 --batch_size 32 --epochs 100 --optimizer 'momentum' --lr_scheduling --check_point
```

### Testing
- Testing model to evaluate the performance in test set
```
python3 test.py --data_path '{dataset directory}' --model '{the one of 4 models}' --weight './runs/exp/weights/best.pt' --img_size 224 --num_workers 8 --batch_size 32 --num_classes 100
```

### Acknowledgements
- 데이터셋 수집에 도움 주신 분들: [이마트24 용인 명지대점](https://map.naver.com/v5/search/%EC%9D%B4%EB%A7%88%ED%8A%B824%20%EC%9A%A9%EC%9D%B8%20%EB%AA%85%EC%A7%80%EB%8C%80%EC%A0%90/place/1019132650?c=15,0,0,2,dh&isCorrectAnswer=true), [하나로마트 오산농협본점](https://map.naver.com/v5/search/%EC%98%A4%EC%82%B0%20%EB%86%8D%ED%98%91%20%ED%95%98%EB%82%98%EB%A1%9C%EB%A7%88%ED%8A%B8%20%EB%B3%B8%EC%A0%90/place/13373937?c=15,0,0,2,dh&placePath=%3Fentry%253Dpll)