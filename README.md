# Concrete Damage Detection using YOLOv8 and YOLOv11 🚧🧠

This project compares the performance of two deep learning models—**YOLOv8** and **YOLOv11**—for detecting surface damage on concrete structures, focusing on two key defect types: **crack** and **spall**. The goal is to evaluate which model is more accurate and efficient for real-world structural inspections.

## 📌 Objective

To analyze and compare the detection performance, speed, and accuracy of YOLOv8 vs. YOLOv11 in identifying concrete surface defects.

## 🧠 Models Used

- **YOLOv8** (baseline)
- **YOLOv11** (latest version with improved architecture)

## 🗂️ Dataset

- **Total images**: 776
- **Classes**: `Crack`, `Spall`
- **Annotation tool**: Roboflow
- **Split**: 90% training / 10% validation + test

## ⚙️ Training Configuration

- Epochs: 40  
- Image Size: 640  
- Batch Size: 16  
- Learning Rate: 0.005  
- Training options: `rect`, `cache`

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

## ⚡ Speed Comparison

| Model     | Training Time (40 epochs) | Inference Speed (ms/image) | Model Size | FLOPs |
|-----------|----------------------------|-----------------------------|------------|-------|
| YOLOv8    | 0.109 hrs (6.5 mins)       | 83.7 ms (GPU)               | 6.2 MB     | 8.1 G |
| YOLOv11   | 0.119 hrs (7.1 mins)       | 2.9 ms (GPU)                | 5.5 MB     | 6.3 G |

## 🖼️ Sample Outputs

| Model | Ground Truth vs Prediction |
|-------|----------------------------|
| YOLOv8 | ![YOLOv8](results - YOLOv8/val_batch0_pred.jpg) vs  ![YOLOv8](results - YOLOv8/val_batch0_labels.jpg) |
| YOLOv11 | ตี้มาใส่ด้วย |

## 💡 Conclusion

- **YOLOv11** is more suitable for **real-time, safety-critical applications** like bridge or infrastructure inspections.
- **YOLOv8** remains a valid alternative for general use, especially in low-resource environments.

## 📌 Future Work

- Fine-tune YOLOv11 for better Spall detection
- Expand dataset to more damage types (e.g., rebar, joint cracks)
- Explore data augmentation and domain-specific tuning

---

## 🧾 Citation

