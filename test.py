import os
import glob
import argparse
import ipdb
# Kerasa / TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model
from layers import BilinearUpSampling2D
from loss import depth_loss_function
from utils import predict, load_images, display_images, save_images
from matplotlib import pyplot as plt
import numpy as np

# Argument Parser
parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
parser.add_argument('--model', default='kitti.h5', type=str, help='Trained Keras model file.')
parser.add_argument('--input', default='sample/images/*png', type=str, help='Input filename or folder.')
args = parser.parse_args()

# Custom object needed for inference and training
custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': depth_loss_function}

print('Loading model...')

# Load model into GPU / CPU
model = load_model(args.model, custom_objects=custom_objects, compile=False)

print('\nModel loaded ({0}).'.format(args.model))

# Input images
inputs = load_images( glob.glob(args.input) )
ipdb.set_trace()
print('\nLoaded ({0}) images of size {1}.'.format(inputs.shape[0], inputs.shape[1:]))

for input_image in range(inputs.shape[0]):
    img = np.expand_dims(inputs[input_image], axis=0)
    outputs = predict(model, img)
    save_images('image_'+str(input_image), outputs)

# Compute results

# Display results
# viz = display_images(outputs.copy(), inputs.copy())
# plt.figure(figsize=(10,5))
# plt.imsave('depth_pred.png', viz)
# plt.show()
