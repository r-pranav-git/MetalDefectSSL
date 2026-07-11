# METALYX
## Self-Supervised Contrastive Learning for Metal Surface Defect Classification

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Project Overview

METALYX is a deep learning research project focused on automatic metal surface defect classification using **Self-Supervised Contrastive Learning (SSL)**. Traditional supervised learning requires a large amount of labeled data, which is expensive and time-consuming to obtain in industrial environments.

This project leverages self-supervised learning to learn meaningful visual representations from unlabeled metal surface images. The learned representations are then fine-tuned for defect classification using a small labeled dataset.

---

## Problem Statement

Manual inspection of metal surfaces is:

- Time-consuming
- Expensive
- Inconsistent
- Prone to human error

Deep learning offers automated inspection, but supervised models require thousands of labeled images.

METALYX addresses this challenge using Self-Supervised Contrastive Learning, reducing dependence on labeled datasets while maintaining high classification performance.

---

## Objectives

- Develop an automated metal surface defect classification system.
- Learn feature representations using Self-Supervised Contrastive Learning.
- Fine-tune the pretrained encoder using labeled defect images.
- Compare performance with traditional supervised learning.
- Improve classification accuracy using representation learning.

---

## Dataset

This project uses the **NEU Surface Defect Database**.

### Defect Classes

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

---

## Methodology

The complete workflow consists of the following stages:

1. Dataset Collection
2. Data Preprocessing
3. Data Augmentation
4. Self-Supervised Contrastive Pretraining
5. Feature Representation Learning
6. Fine-tuning for Classification
7. Model Evaluation

---

## Project Architecture

Dataset
↓
Image Preprocessing
↓
Data Augmentation
↓
Contrastive Learning
↓
ResNet18 Encoder
↓
Feature Representation
↓
Fine-Tuning
↓
Defect Classification

---

## Technology Stack

- Python
- PyTorch
- TorchVision
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Google Colab

---

## Project Structure

```
MetalDefectSSL/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── results/
│
├── README.md
│
└── requirements.txt
```

---

## Evaluation Metrics

The model will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## Current Progress

- [x] Literature Survey
- [x] Project Planning
- [ ] Dataset Preparation
- [ ] Data Preprocessing
- [ ] Self-Supervised Pretraining
- [ ] Fine-Tuning
- [ ] Model Evaluation
- [ ] Documentation

---

## Future Improvements

- Vision Transformer (ViT)
- BYOL Framework
- SimSiam Framework
- Real-time Industrial Inspection
- Explainable AI (Grad-CAM)

---

## References

1. Self-Supervised Contrastive Learning for Metal Surface Defect Classification
2. NEU Surface Defect Database
3. PyTorch Documentation
4. ResNet18 Architecture

---

## Team Members

- R Pranav(46) 
- Patrick Davis Jerry(45)

---

## Guide

Prof. NADERA BEEVI S

---

## License

This project is developed for academic and research purposes.
