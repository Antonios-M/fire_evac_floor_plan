# Fire Evacuation Prediction on Architectural Floor Plans

This repository aims to provide a workflow and tools for emergency evacuation performance prediction of architectural floor plans. The key steps are modelling evacuation using the graph-representation of the floor plan and pre-evacuation using stochastic methods such as Markov Chain Monte Carlo simulations. Evac and pre-evac times are used to label floor plan images, on which two simple CNN architectures are trained to predict evacuation performance.

** Project Report: ** https://issuu.com/tonymavr/docs/antonios_mavrotas_-_6047807_-_ciid_report
![fig3](https://github.com/user-attachments/assets/c27b2752-0ae6-4858-a3e6-73679c0ff4e4)


## Dataset

The Swiss Dwelling Dataset (SDDS) https://zenodo.org/records/7070952

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
