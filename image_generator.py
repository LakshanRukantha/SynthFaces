#!/usr/bin/env python
# coding: utf-8

import os  # For interacting with the operating system
import numpy as np  # For numerical operations
from PIL import Image  # For working with images
import tensorflow as tf  # For deep learning framework
from tensorflow.keras import layers  # For defining neural network layers
from keras.models import Sequential  # For creating sequential models
from tensorflow.keras.layers import (  # For specific layer types
    Conv2D,  # Convolutional layer
    Flatten,  # Flatten layer
    Dense,  # Dense layer
    LeakyReLU,  # Leaky ReLU activation
    Reshape  # Reshape layer
)
import matplotlib.pyplot as plt  # For plotting and visualization

# Set the path to your image dataset directory
dataset_dir = '../images'

