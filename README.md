# [DTH-YOLO: Enhanced YOLOv8n with Dynamic Task-Aligned Head for mouseholes Detection]()
## Introduction
The demand of applying semantic segmentation model on mobile devices has been increasing rapidly. Current
state-of-the-art networks have enormous amount of parameters, hence unsuitable for mobile devices, while other small
memory footprint models follow the spirit of classification network and ignore the inherent characteristic of semantic
segmentation. To tackle this problem, we propose a novel Context Guided Network (CGNet), which is a light-weight
and efficient network for semantic segmentation. We first propose the Context Guided (CG) block, which learns the
joint feature of both local feature and surrounding context, and further improves the joint feature with the global context.
Based on the CG block, we develop CGNet which captures contextual information in all stages of the network and
is specially tailored for increasing segmentation accuracy. CGNet is also elaborately designed to reduce the number
of parameters and save memory footprint. Under an equivalent number of parameters, the proposed CGNet significantly outperforms existing segmentation networks. Extensive experiments on Cityscapes and CamVid datasets verify the effectiveness of the proposed approach. Specifically, without any post-processing and multi-scale testing, the proposed CGNet achieves 64.8% mean IoU on Cityscapes with less than 0.5 M parameters.


## Installation
1. Install PyTorch
- Env: PyTorch\_2.3.1; cuda\_12.1; cudnn\_9.6; python\_3.11.11; mmcv\_2.1.0


## Citation
If DTH-YOLO is useful for your research, please consider citing:
```

```
## License

This code is released under the Apache License. See [LICENSE](LICENSE) for additional details.


Additionally, this project uses the following third-party open-source components:

RepViTBlock
License: Apache License 2.0
Detailed information and full license text: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
Location: ultralytics/nn/modules/block.py
Original project link: https://github.com/THU-MIG/RepViT

ContextGuidedBlock_Down
License: MIT
Detailed information and full license text: [MIT License](https://opensource.org/licenses/MIT)
Location: ultralytics/nn/modules/block.py
Original project link: https://github.com/wutianyiRosun/CGNet

TaskDecomposition
License: Apache License 2.0
Detailed information and full license text: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
Location: ultralytics/nn/modules/head.py
Original project link: https://github.com/fcjian/TOOD


