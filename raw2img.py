import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Converts All Raw Images in Directory to Output Directory.')

#parser.add_argument('--input', metavar = 'input', type = str, default = 'D:\\top')
#parser.add_argument('--output', metavar = 'output', type = str, default = 'D:\\top')

#file_input = 'D:\\Server Data Copy 12-12\\12-02-TREADMILL\\z.12.02.20.JWC - EVENT 4\\'
#file_output = 'D:\\Server Data Copy 12-12\\12-02-TREADMILL\\z.12.02.20.JWC - EVENT 4 - converted\\'

files = 'E:\\Q175\\Open Field\\1.21.21 - bottom\\'
img_dims = (1080, 1440)
for folder in tqdm(os.listdir(files)):
	file_input = os.path.join(files, folder)
	if 'converted' in folder:
		continue
	outfolder = folder + ' - converted'
	file_output = os.path.join(files, outfolder)
#args = parser.parse_args()
	try:
		os.makedirs(file_output)
		print('Output Directory Created')
	except OSError as e:
		print('Output Directory Already Exists')
	file_input = file_input + '\\'
	file_output = file_output + '\\'
	print(file_input)
	print(file_output)
	for img in tqdm(os.listdir(file_input)):
		name = img
		folder = name.split('-')[0]
		img = file_input + img
		
		try:
			img = np.fromfile(img, dtype = np.uint8).reshape(img_dims)
		except Exception as e: 
			#img = np.fromfile(img, dtype = np.uint8)
			print(np.fromfile(img, dtype = np.uint8).shape)
			continue
		#plt.imshow(img)
		#plt.show()
		
		try:
			os.makedirs(file_output + folder)
			print('Output Subdirectory Created')
		except OSError as e:	
			pass
		cv2.imwrite(file_output + folder + '\\' + name.split('-')[-1][:-4] +'.png', img)