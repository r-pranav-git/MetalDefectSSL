"""
Project Configuration
METALYX - Self-Supervised Contrastive Learning for Metal Surface Defect Classification
"""

# Dataset
DATASET_PATH = "datasets/NEU-CLS"

# Image Settings
IMAGE_SIZE = 224

# Training Parameters
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 0.001

# Model
BACKBONE = "resnet18"

# Device
DEVICE = "cuda"
