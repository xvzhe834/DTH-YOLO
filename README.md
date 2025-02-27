# [DTH-YOLO: Enhanced YOLOv8n with Dynamic Task-Aligned Head for mouseholes Detection]()
## Introduction
In recent years, the increasing number of mouseholes in grassland areas has accelerated desertification, 
leading to a decline in grassland productivity and severely impacting the economic benefits of herders. 
Therefore, accurately and efficiently detecting and locating mouseholes has become an urgent research problem. 
UAV photography, with its advantages of wide coverage and flexibility, has gradually become an effective tool 
for mousehole detection. However, due to varying flight altitudes causing significant changes in target scale, 
severe occlusion of targets, and the small size of burrows, aerial detection faces high rates of missed and false 
detections, posing a significant challenge to burrow identification. To address these issues, we propose the 
DTH-YOLO model, based on YOLOv8n. First, we replace the original detection head with the Dynamic Task-Aligned 
Head (DTH) to enhance feature alignment across different tasks and improve detection accuracy. Secondly, we 
design the C2f-RVB module to optimize the feature extraction process, significantly reducing model parameters 
and computational costs. Finally, we introduce the Context Guided Block (CGB) for downsampling, effectively 
capturing contextual information in the target area, thereby improving detection performance for small objects.
Experimental results show that, on a custom aerial mousehole dataset, the DTH-YOLO model achieves an 8.5\% increase 
in mAP@0.5, a 5.6\% improvement in precision, a 42\% reduction in parameters, and a 22\% decrease in GFLOPs compared 
to the baseline YOLOv8n model. Furthermore, ablation studies demonstrate the effectiveness of each proposed module.


## Installation
1. Install PyTorch
- Env: PyTorch\_2.3.1; cuda\_12.1; cudnn\_9.6; python\_3.11.11; mmcv\_2.1.0


## Citation
If DTH-YOLO is useful for your research, please consider citing:
```

```


