# TomatoPlant Disease Detection: My Deep Learning Journey
## Introduction
Welcome to my TomatoPlant Disease Detection project! Join me as I delve into the world of Deep Learning, where I've developed a model using TensorFlow and Keras to accurately detect diseases in tomato plants. Through the power of Convolutional Neural Networks (CNNs) and Dense Layers, I've achieved impressive results in classifying these plant diseases.

## Dataset Exploration
I began by curating a diverse dataset that encompasses various tomato plant diseases, including:

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
My model architecture was carefully crafted to ensure optimal disease classification. I harnessed the potential of multiple Convolutional Layers, skillfully paired with Max Pooling Layers, to create a flattened vector. This paved the way for a series of Dense Layers, responsible for both feature extraction and precise classification.

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/92b21a92-195a-4bdc-b857-3dfd8d7f846f)


## Training, Validation, and Triumph

My journey continued as I embarked on the training and evaluation phase:

* I harnessed the power of ```tf.keras.preprocessing.image_dataset_from_directory``` for seamless data loading and labeling.
* Through careful partitioning, I established dedicated training, validation, and test sets.
* My images underwent a transformation, being resized to a harmonious 256x256 and skillfully normalized.

The culmination of my efforts yielded remarkable accuracy results:
* Test accuracy: **97.95%**
* Validation accuracy: **92.55%**
* Test accuracy: **92.94%**

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/8ad1d4d7-a1ea-46fd-b1a3-6bb34e988a4f)


## Envisioning Predictions and Visualization
The fruits of my labor came to life as I visualized model predictions, creating plots that showcased confidence levels, actual labels, and the predicted labels. This visual insight added a layer of clarity and understanding to my classification endeavors.

![image](https://github.com/mohd-arham-islam/TomatoPlant/assets/111959286/da7b6744-d9f3-4970-9b7d-bf7a897e9414)


## Ensuring Model Persistence
To secure my work, I preserved my trained model in the enduring **.h5** format. This thoughtful preservation strategy ensures easy access, retrieval, and deployment whenever the need arises.

## Embarking on a FastAPI Adventure
My journey took a dynamic turn as I embarked on the creation of a FastAPI server. This ingenious solution allows users to input an image, receiving in return both the confidence level and the predicted label. This seamless integration empowers real-time disease detection on new images, bridging the gap between technology and agriculture.

## Reflections and Future Growth
As my TomatoPlant Disease Detection project reaches its conclusion, I'm left with a sense of accomplishment and a vision for the future. My journey into the realm of Deep Learning has illuminated the potential for innovation in agriculture. I encourage you to join me in this quest to enhance crop health, improve food security, and create lasting positive change.
