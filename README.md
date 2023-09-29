# Diabetes Classifier with REST API

## Overview
The establishment of a REST API tailored for the precise classification of diabetes patients based on input parameters marks a significant milestone in the realm of cutting-edge healthcare analytics and patient care. This versatile API empowers healthcare professionals, researchers, and software developers alike, equipping them with the tools of machine learning and data analysis to facilitate data-driven decisions in the realm of diabetes diagnosis and treatment.

## Error
After creating a pre-trained model using a pipeline, I ran into an issue while working on the 'api.py' file. Specifically, I received an error message that said, 'This StandartScaler instance is not fitted yet,' and despite my efforts, I couldn't find a solution to this problem. It's worth noting that the model works correctly when executed within the source code, but when I attempt to integrate it into the 'app.py' file, it fails to function as expected.

## Information Of Model
My model is designed to navigate through the complexities of scattered data effectively. It starts by preprocessing the data, which includes the critical step of eliminating irrelevant data points to ensure a cleaner and more focused dataset. This initial data cleaning stage is vital for enhancing the model's overall performance. After identifying the optimal hyperparameters, the model is then trained using the clean data. This training process helps the model learn the underlying patterns and relationships within the data, enabling it to make accurate predictions or classifications.