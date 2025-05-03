# Concrete Damage Detection using YOLOv8 and YOLOv11 🚧🧠

This project compares the performance of two deep learning models—**YOLOv8** and **YOLOv11**—for detecting surface damage on concrete structures, focusing on two key defect types: **crack** and **spall**. The goal is to evaluate which model is more accurate and efficient for real-world structural inspections.

**Report Link:** https://drive.google.com/file/d/1yDCUpq7zvdnUtfnEfrzoms-qFYAL-aGP/view?usp=sharing

**Presentation Link:** https://www.canva.com/design/DAGkUMcgs_o/2DWEGSc1hvsSVPVqODVxjw/edit?utm_content=DAGkUMcgs_o&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## 📌 Objective

To analyze and compare the detection performance, speed, and accuracy of YOLOv8 vs. YOLOv11 in identifying concrete surface defects.

## 📂 Project Structure

```plaintext
Crack-Detection-YOLOv8/
├── example dataset/
│   ├── train/
│   ├── valid/
│   └── test/
├── result - YOLOv8/
│   ├── confusion_matrix.png
│   ├── PR_curve.png
│   ├── F1_curve.png
│   ├── R_curve.png
│   ├── P_curve.png
│   ├── result.png
│   └── val_batch*_labels/pred.jpg
├── result - YOLOv11/
│   ├── confusion_matrix.png
│   ├── PR_curve.png
│   ├── F1_curve.png
│   ├── R_curve.png
│   ├── P_curve.png
│   ├── result.png
│   └── val_batch*_labels/pred.jpg
├── Crack-detection_finetune.py
├── data.yaml
├── requirements.txt
└── README.md
```

## 🧠 Models Used

- **YOLOv8** (baseline)
- **YOLOv11** (latest version with improved architecture)

## 🗂️ Dataset

- **Total images**: 776
- **Classes**: `Crack`, `Spall`
- **Annotation tool**: Roboflow
- **Split**: 90% training / 10% validation + test

## ⚙️ Training Configuration

- **Epochs**: 40  
- **Image Size**: 640  
- **Batch Size**: 16  
- **Learning Rate**: 0.005  
- **Training options**: `rect`, `cache`

## 📊 Evaluation Metrics

| Metric     | Description |
|------------|-------------|
| Precision  | True Positive / All Predicted Positives |
| Recall     | True Positive / All Actual Positives |
| F1-Score   | Harmonic mean of precision and recall |
| mAP@50     | Average precision at IoU ≥ 0.5 |
| mAP@50–95  | Average precision across IoU thresholds 0.5 to 0.95 |

## ✅ YOLOv8 vs YOLOv11 — Performance Comparison

| Model     | Precision | Recall | mAP@50 | mAP@50–95 |
|-----------|-----------|--------|--------|-----------|
| YOLOv8    | 0.65      | 0.40   | 0.35   | 0.15      |
| YOLOv11   | 0.75      | 0.55   | 0.55   | 0.30      |

> 🟢 **YOLOv11** performs better across almost all metrics, especially in Crack detection and inference speed.

## 🔍 Confusion Matrix Insights

- **YOLOv8**: Struggles with false positives, especially confusing background as Spall.
- **YOLOv11**: Better background separation and Crack classification, though Spall detection still needs improvement.

### 📊 Model Training Performance

| Model Training Performance **YOLOv8**          |             
|------------------------------------------------|
| ![](result%20-%20YOLOv8/Model_Performance.png)     |

| Model Training Performance **YOLOv11**         |             
|------------------------------------------------|
| ![](result%20-%20YOLOv11/Model_Performance.png)    |

### 📌 Confusion Matrix & PR Curve

| Confusion Matrix **YOLOv8**                          | Precision-Recall Curve **YOLOv8**              |
|--------------------------------------------------|--------------------------------------------|
| ![](result%20-%20YOLOv8/confusion_matrix.png)    | ![](result%20-%20YOLOv8/PR_curve.png)      |

| Confusion Matrix **YOLOv11**                          | Precision-Recall Curve **YOLOv11**              |
|---------------------------------------------------|---------------------------------------------|
| ![](result%20-%20YOLOv11/confusion_matrix.png)    | ![](result%20-%20YOLOv11/PR_curve.png)      |

### 🔍 Per-Class Performance Curves

| F1 Score Curve **YOLOv8**                            | Precision Curve **YOLOv8**                       | Recall Curve **YOLOv8**                       |
|--------------------------------------------------|----------------------------------------------|-------------------------------------------|
| ![](result%20-%20YOLOv8/F1_curve.png)            | ![](result%20-%20YOLOv8/P_curve.png)         | ![](result%20-%20YOLOv8/R_curve.png)      |

| F1 Score Curve **YOLOv11**                            | Precision Curve **YOLOv11**                     | Recall Curve **YOLOv11**                       |
|---------------------------------------------------|---------------------------------------------|--------------------------------------------|
| ![](result%20-%20YOLOv11/F1_curve.png)            | ![](result%20-%20YOLOv11/P_curve.png)       | ![](result%20-%20YOLOv11/R_curve.png)      |

## ⚡ Speed Comparison

| Model     | Training Time (40 epochs) | Inference Speed (ms/image) | Model Size | FLOPs |
|-----------|----------------------------|-----------------------------|------------|-------|
| YOLOv8    | 0.109 hrs (6.5 mins)       | 83.7 ms (GPU)               | 6.2 MB     | 8.1 G |
| YOLOv11   | 0.119 hrs (7.1 mins)       | 2.9 ms (GPU)                | 5.5 MB     | 6.3 G |

## 🧪 Sample Predictions

| Ground Truth                                     | **YOLOv8** Predictions                           | **YOLOv11** Predictions                           |
|--------------------------------------------------|----------------------------------------------|----------------------------------------------|
| ![](result%20-%20YOLOv8/val_batch0_labels.jpg)   | ![](result%20-%20YOLOv8/val_batch0_pred.jpg) | ![](result%20-%20YOLOv11/val_batch0_pred.jpg) |


## 💡 Conclusion

- **YOLOv11** is more suitable for **real-time, safety-critical applications** like bridge or infrastructure inspections.
- **YOLOv8** remains a valid alternative for general use, especially in low-resource environments.

## 🧾 Requirements

Install required packages:

```bash
pip install -r requirements.txt
```

Example packages used:

```txt
ultralytics==8.0.20
torch
opencv-python
jupyter
```

## 📌 Future Work

- Expand dataset to more damage types (e.g., rebar, joint cracks)
- Explore data augmentation and domain-specific tuning

---

## 👥 Authors

- **Pinthucha Ruckpintuwat**  
  `Deedeelimm@gmail.com`
- **Parinya Boonpama**  
  `smg.ttmt@gmail.com`  
