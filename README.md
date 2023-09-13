# TomatoPlant Disease Detection: My Deep Learning Journey
## Introduction
This project demonstrates the use of deep learning to detect diseases in tomato plants. The model was trained on a dataset of images of tomato plants with various diseases, and it achieved an accuracy of 92.94% on a test set.

## Dataset Exploration
The dataset used for this project was collected from the PlantVillage dataset. The dataset contains images of tomato plants with nine different diseases:

* **Bacterial Spot**
* **Curl Virus**
* **Early Blight**
* **Healthy**
* **Late Blight**
* **Leaf Mold**
* **Mosaic Virus**
* **Septorial Leaf Spot**
* **Two Spotted Spider Mite**

## Crafting the Model Architecture
The model architecture used for this project is a convolutional neural network (CNN). I harnessed the potential of multiple Convolutional Layers, skillfully paired with Max Pooling Layers, to create a flattened vector. This paved the way for a series of Dense Layers, responsible for both feature extraction and precise classification.

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/92b21a92-195a-4bdc-b857-3dfd8d7f846f)


## Training and Validation

* The powerful ```tf.keras.preprocessing.image_dataset_from_directory``` facilitated seamless data loading and labeling.
* Through prudent data partitioning, distinct sets for training, validation, and testing were established.
* A harmonious resizing of images to 256x256 dimensions, combined with skillful normalization, enhanced data quality.

The model yielded remarkable accuracy results:
* Training accuracy: **97.95%**
* Validation accuracy: **92.55%**
* Test accuracy: **92.94%**

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/8ad1d4d7-a1ea-46fd-b1a3-6bb34e988a4f)


## Envisioning Predictions and Visualization
Visualization played a pivotal role in this project as model predictions were elegantly depicted through plots, showcasing confidence levels, actual labels, and the predicted labels. This visual insight added depth and clarity to the classification process.

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/da7b6744-d9f3-4970-9b7d-bf7a897e9414)


## Ensuring Model Persistence
I saved my trained model in the enduring **.h5** format. This thoughtful preservation strategy ensures easy access, retrieval, and deployment whenever the need arises.

## Embarking on a FastAPI Adventure
This journey took an innovative turn as a **FastAPI** server was developed. This ingenious solution empowers users to input an image, receiving both the confidence level and the predicted label in real-time. This integration seamlessly bridges the gap between cutting-edge technology and agriculture.

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/648be52e-b601-4d21-8e93-fa20eabbaeb2)


## Reflections and Future Growth
As my TomatoPlant Disease Detection project reaches its conclusion, I'm left with a sense of accomplishment and a vision for the future. My journey into the realm of Deep Learning has illuminated the potential for innovation in agriculture. I encourage you to join me in this quest to enhance crop health, improve food security, and create lasting positive change.
