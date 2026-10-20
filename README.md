# METALYX
## Self-Supervised Contrastive Learning for Metal Surface Defect Classification

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![Status](https://img.shields.io/badge/Status-Research%20Evaluation-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Project Overview

METALYX is an academic research project focused on automated metal surface defect classification using **Self-Supervised Contrastive Learning (SimCLR)** and geometric feature extraction using **B-spline curves**.

The project investigates whether combining deep visual representations learned by a neural network with handcrafted geometric descriptors can improve the classification of steel surface defects.

The experimental study compares three feature representations:

1. B-spline geometric features alone.
2. SimCLR deep features alone.
3. A concatenation of SimCLR and B-spline features.

The project uses the NEU Surface Defect Database and evaluates the approaches using a common downstream classification protocol.

---

## Problem Statement

Manual inspection of metal surfaces can be time-consuming, expensive, inconsistent, and prone to human error. Automated defect classification can support industrial quality inspection, but obtaining large amounts of labeled data can be costly.

METALYX investigates self-supervised representation learning as a way to learn useful image features and evaluates whether geometric surface information can complement learned deep features.

---

## Objectives

- Develop an automated steel surface defect classification pipeline.
- Learn visual representations using SimCLR contrastive learning.
- Extract geometric descriptors using B-spline-based feature extraction.
- Compare B-spline-only, SimCLR-only, and combined feature representations.
- Evaluate classification performance using accuracy, precision, recall, F1-score, and confusion matrices.
- Analyze the benefits and limitations of combining deep and geometric features.

---

## Dataset

The project uses the **NEU Surface Defect Database (NEU-DET)**.

The dataset contains six steel surface defect categories:

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

The recorded feature-comparison experiment used:

- **Training images:** 1,440
- **Validation images:** 360
- **Number of classes:** 6

The validation results reported below refer to this experiment. The validation set should not be interpreted as an independent test set.

---

## Methodology

### 1. Dataset Preprocessing

The dataset is loaded and prepared for model training, feature extraction, and downstream classification.

### 2. SimCLR Self-Supervised Learning

SimCLR learns visual representations by training an encoder to bring augmented views of the same image closer in projection space while distinguishing views from different images.

The implemented training pipeline uses a ResNet-18 encoder and a projection head with the NT-Xent contrastive loss.

### 3. Deep Feature Extraction

The trained encoder is used to extract **512-dimensional** feature vectors from steel surface images.

### 4. B-spline Geometric Feature Extraction

A separate feature-extraction pipeline represents geometric information from image contours using B-spline curve fitting and derives a **10-dimensional** descriptor.

Some images produced all-zero B-spline feature vectors in the recorded comparison. This remains a known limitation requiring further investigation.

### 5. Feature Fusion

The SimCLR and B-spline feature vectors are concatenated:

- SimCLR features: 512 dimensions
- B-spline features: 10 dimensions
- Combined representation: 522 dimensions

### 6. Downstream Classification

The three feature representations are evaluated using Logistic Regression with feature standardization under the recorded comparison protocol.

### 7. Evaluation

The evaluation includes accuracy, macro-precision, macro-recall, macro-F1, weighted-F1, classification reports, and confusion matrices.

---

## Project Architecture

```text
NEU-DET Steel Surface Images
             |
       Preprocessing
             |
      +------+------+
      |             |
   SimCLR        B-spline
   Encoder       Extraction
      |             |
  512-D Deep     10-D Geometric
   Features        Features
      |             |
      +------+------+
             |
      Feature Concatenation
          (522-D)
             |
    Logistic Regression
             |
    Defect Classification
             |
       Model Evaluation
```

The B-spline-only and SimCLR-only representations are also evaluated independently as baselines.

---

## Experimental Results

The following are the recorded results from the corrected three-method validation comparison.

| Method | Feature dimensions | Validation accuracy | Macro-F1 |
|---|---:|---:|---:|
| B-spline-only | 10 | 73.89% | 72.10% |
| SimCLR-only | 512 | 92.78% | 92.69% |
| SimCLR + B-spline | 522 | **95.28%** | **95.25%** |

In this comparison, the combined representation achieved the highest validation accuracy and macro-F1 score.

The results suggest that geometric descriptors may complement learned deep representations. However, the presence of all-zero B-spline feature vectors is an important limitation when interpreting this improvement.

These figures are validation metrics from the recorded experiment, not independent-test performance or a guarantee of performance on industrial data.

### Additional Encoder Experiment

A separate ShuffleNetV2-based SimCLR/downstream classification experiment was also conducted. Its results are treated separately because its data split and evaluation protocol have not yet been fully verified against the main three-method comparison.

---

## Repository Structure

```text
MetalDefectSSL/
├── notebooks/
│   ├── 01_dataset_preprocessing.ipynb
│   ├── 02_simclr_training_v2.ipynb
│   ├── 03_downstream_classification_Corrected (1).ipynb
│   ├── METALYX_Notebook_1_BSpline_Only (1).ipynb
│   ├── METALYX_Corrected_Fair_Comparison.ipynb
│   ├── METALYX_Notebook_2_SimCLR_BSpline_Fusion (1).ipynb
│   └── Metalyx_Curve_Detection.ipynb
├── datasets/
├── losses/
├── models/
├── utils/
├── README.md
├── config.py
├── requirements.txt
├── train.py
└── test.py
```

The repository may contain additional exploratory or earlier notebook versions. The corrected fair-comparison notebook is intended to document the primary three-method comparison, while the earlier fusion notebook preserves the development history.

---

## How to Run

The notebooks were developed for a Python environment such as Google Colab.

1. Clone or download the repository.
2. Install the required dependencies from `requirements.txt`.
3. Obtain the NEU-DET dataset and configure its path in the relevant notebook.
4. Run dataset preprocessing.
5. Run the SimCLR training notebook if reproducing pretraining.
6. Run downstream classification and B-spline feature extraction as required.
7. Run the corrected fair-comparison notebook to evaluate the three feature representations.

**Reproducibility note:** Confirm that the checkpoint used for feature extraction corresponds to the intended training run and that its pretraining data excludes the validation images before claiming a fully verified reproduction.

---

## Limitations

- Some images produced all-zero B-spline feature vectors; the cause has not yet been established.
- The reported comparison uses a validation set rather than a separate independent test set.
- The exact provenance of the checkpoint used in the current comparison requires verification.
- The ShuffleNetV2 experiment has not been confirmed to use an evaluation protocol directly comparable with the main comparison.
- Further testing is needed to establish generalization beyond the dataset and experimental setup used here.

---

## Future Work

- Improve the reliability of B-spline feature extraction.
- Investigate images that produce all-zero geometric descriptors.
- Verify checkpoint provenance and training/validation separation.
- Evaluate the final approach on independent test data.
- Investigate alternative encoders and representation-learning methods.
- Explore explainability methods and potential industrial deployment.

---

## References

1. NEU Surface Defect Database (NEU-DET).
2. SimCLR: A Simple Framework for Contrastive Learning of Visual Representations.
3. ResNet architecture and PyTorch/TorchVision documentation.
4. B-spline curve representation and geometric feature extraction literature.

Add the full bibliographic details of the specific papers used in the project's literature survey before final submission.

---

## Team Members

- R. Pranav (46)
- Patrick Davis Jerry (45)

## Project Guide

Prof. Nadera Beevi S.

---

## License

This project includes an MIT license badge. Ensure that a corresponding `LICENSE` file exists in the repository before representing the repository as licensed under the MIT License.

The project is developed for academic and research purposes.
