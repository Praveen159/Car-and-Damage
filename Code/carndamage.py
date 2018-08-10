# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
#from keras.applications.vgg16 import VGG16
from keras import applications
from keras.preprocessing.image import img_to_array,load_img
#from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model

img_width=224
img_height=224
model1 = applications.VGG16(weights='imagenet')
Damage=load_model("./models/epoch_2.h5")


def pred_car(img):
    im=load_img(img,target_size=(224,224))
    x=img_to_array(im)
    x=x.reshape((1,)+x.shape)
    x = preprocess_input(x)
    model1._make_predict_function()
    pred=model1.predict(x)
    label=decode_predictions(pred)
    label = label[0][0]
    #print('%s (%.2f%%)' % (label[1], label[2]*100))
    return label[1],label[2]

def pred_total(img1):
	carvalue=pred_car(img1)
	l=['car','sports_car']
	if carvalue[0] in l:
		car="Uploaded Image is Car"
		img_256=load_img(img1,target_size=(256,256))
		x=img_to_array(img_256)
		x=x.reshape((1,)+x.shape)/255
		predi_damage=Damage.predict(x)
		if predi_damage<0.7:
			damag="Car Got Damaged"
			return car,damag
		else:
			c="Please Submit  damaged  CAR Image"
			return car,c
	else:
		return carvalue[0]
	
#output=pred_total("D:/DS/Train_Images/CarDentImages/CarDentImages1.jpg")
#"The Uploaded Image is {0} with Probability {1}".format(carvalue[0],carvalue[1]



