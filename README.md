# Assignment1

## Task 1.1

* Bounding Box image
* ![image](https://user-images.githubusercontent.com/66863370/159151420-ce696d6e-fe2a-426b-9dd8-3921307fa190.png)

* Transparent Polygon image
* ![image](https://user-images.githubusercontent.com/66863370/159151453-f1bc5524-e150-4f6f-98d3-3ba9945e6473.png)

To be written soon......

## Task 2.1
a) Training on original data 
* Original data: https://www.kaggle.com/anujms/car-damage-detection
* Class weights : https://drive.google.com/uc?export=download&id=1V1t46Zt5TNaCLoy0lFh5N4KqAK6QWYjs
* Dataset : train: 920 damaged, 920 not_damaged
            val:   230 damaged, 230 not_damaged
* Model: CNN-based with 4 convolutional layers + 4 MaxPool layers + 1FC + 1 Hidden layer, Loss-function = Binary cross entropy    
* Evaluation metrics : train_accuracy = 35.19% , val_accuracy = 26.09 % after 20 epochs

b) Data Augmentation (to increase variation in the available dataset)
* rotation range = upto 40 degrees
* shearing_range = 0.2 degree (=slant angle along which image is stretched)
* zoom_range = 0.2 ( means magnification)
* horizontal_flip =True // generates images which are randomly horizontally flipped
* brightness_range = (0.5, 1.5)  // Brightness shift from 0.5 to 1.5
* ![image](https://user-images.githubusercontent.com/66863370/159150470-d188e16f-f758-4045-9ee5-c3e295cad58d.png)

c) Training on Augmented data
* Dataset: train = 2309 damaged, 2309 not_damaged
*           val = 577 damaged, 629 not_damaged
* Class weigths: https://drive.google.com/uc?export=download&id=1V1t46Zt5TNaCLoy0lFh5N4KqAK6QWYjs
* Model: same as before
* Evaluation metrics: Binary accuracy on validation set: 71.64 % (after 20 epochs)
*            precison =  0.38128249566724437
            recall =  0.43912175648702595
            f1-score =  0.40816326530612246

