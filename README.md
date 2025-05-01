# Concrete Crack Detection using YOLOv8 and YOLOv11

This project uses YOLOv8 to detect two types of damage on concrete surfaces: **Crack** and **Spall**.

## Dataset
- 2 classes: Crack, Spall
- Annotated in YOLO format

## Training Settings
- 40 epochs, image size: 640, batch size: 16
- Learning rate: 0.005

## Results (YOLOv8 vs YOLOv11)
| Class  | Precision | Recall | mAP50 |
|--------|-----------|--------|--------|
| Crack  | 0.88      | 0.85   | 0.462  |
| Spall  | 0.70      | 0.65   | 0.260  |

## Inference Example

![Result](results/inference_example.jpg)
