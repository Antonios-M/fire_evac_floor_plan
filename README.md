# Fire Evacuation Prediction on Architectural Floor Plans

This repository contains code and resources for predicting fire evacuation routes on architectural floor plans using machine learning techniques.

## Table of Contents

- Introduction
- Features
- Installation
- Usage
- Contributing
- License

## Introduction

The goal of this project is to develop a model that can predict the most efficient evacuation routes in case of a fire emergency. This can help in designing safer buildings and improving emergency response strategies.

## Features

- **Markov Chain Model**: Implements a Markov Chain to simulate evacuation routes.
- **CNN Model**: Uses Convolutional Neural Networks (CNN) to analyze floor plans.
- **Dataset Creation**: Tools for creating and labeling datasets from architectural plans.
- **Visualization**: Visualize predicted evacuation routes on floor plans.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Antonios-M/fire_evac_floor_plan.git
cd fire_evac_floor_plan
pip install -r requirements.txt
```

## Usage

1. **Creating the Dataset**:
    - Use `main_creating_dataset.ipynb` to create and label your dataset.
2. **Predicting Evacuation Routes**:
    - Use `MarkovChainClass.py` to simulate evacuation routes based on the trained model (will affect labels, and is stochastic).
3. **Training the Model**:
    - Run `main_CNN_model.ipynb` to train the CNN model on your dataset.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to customize this template to better fit your project’s specifics! If you need any more details or adjustments, let me know.
