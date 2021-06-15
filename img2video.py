

import cv2
import os
from tqdm import tqdm
import matplotlib.pyplot as plt


main_folder = "E:\\Q175\\Open Field\\2.12.21-AAR-bottom\\"
fps = 200

for folder in tqdm(os.listdir(main_folder)):
	if 'converted' in folder:
		folder = os.path.join(main_folder, folder)
		for angle in os.listdir(folder):
			
			input_folder = os.path.join(folder, angle)


			print(input_folder)
			imgs = os.listdir(input_folder)
			imgs.sort(key = lambda x: int(x.split('.')[0]))
			frame = cv2.imread(os.path.join(input_folder, imgs[0]))
			height, width, layers = frame.shape
			print(input_folder)
			fourcc = cv2.VideoWriter_fourcc(*'mp4v')
			video = cv2.VideoWriter(os.path.join(folder, angle + '.mp4'), fourcc, fps, (width,height))

			for image in tqdm(imgs):
			    video.write(cv2.imread(os.path.join(input_folder, image)))

			#cv2.destroyAllWindows()
			video.release()