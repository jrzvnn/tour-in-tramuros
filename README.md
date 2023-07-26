# Tour-in-tramuros

Welcome to the GitHub repository for our project on object detection of historical buildings in Intramuros using [YOLOv8](https://github.com/ultralytics/ultralytics). In this project, we have developed a model that can accurately identify prominent building attractions in the historical site of Intramuros.

![demo](demo.gif)
## Scope 

The model is trained and tested to identify the following historical buildings and landmarks within Intramuros:

1. Casa Manila
2. Fort Santiago
3. King Charles IV Monument
4. Manila Cathedral
5. Palacio de Gobernador
6. San Agustin Church

Feel free to add more landmarks to the dataset for further analysis and detection. The dataset is annotated and preprocess using [Roboflow](https://roboflow.com/).

## Requirements

Before using this repository, make sure you have the following prerequisites installed:
* Python (>=3.9)
* Pip (Python package manager)


## Usage

To use the repository, follow these steps:

1. Clone the repository to your local machine using:
```
git clone https://github.com/your_username/intramuros-object-detection.git
cd intramuros-object-detection
```
2. To set up the required environment and install dependencies, you can use the provided `requirements.txt` file. Run the following command:
```
pip install -r requirements.txt
```
3. The dataset is already available in the repository and is preprocessed in YOLOv8 format.
4. Train the YOLOv8 model using the `train_colab.ipynb` provided in the repository.
5. Additionally, you can use the `main.py` script to display the webcam frames with real-time building detection in Intramuros.
For a more interactive experience, you can run the `app.py` script to access the Streamlit web application for real-time webcam detection of historical buildings. To run it: 
```
streamlit run app.py
```
## Contributing

We welcome contributions from the community! If you find any issues or want to add improvements, feel free to create a pull request. For major changes, please open an issue to discuss the proposed changes first.
