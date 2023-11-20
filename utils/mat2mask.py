import os
import scipy.io as scio
from PIL import Image
import numpy as np
import cv2
from tqdm import trange

# 将CrackForest mat格式的mask转换为png格式

# dataFile = r'E:\defect_datasets\datasets\seg\CrackForest-dataset-master\groundTruth\002.mat' # 单个的mat文件
# data = scio.loadmat(dataFile)
# mask = data['groundTruth']
# # print(mask)
# mask_8bit = cv2.normalize(mask[0][0][0].astype(np.float32), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)


src_dir = r'E:\defect_datasets\datasets\seg\CrackForest-dataset-master\groundTruth'
dst_dir =r'E:\defect_datasets\datasets\seg\CrackForest-dataset-master\image'
for i in trange(len(os.listdir(src_dir))):
    file_name = os.listdir(src_dir)[i]
    dataFile = os.path.join(src_dir, file_name)
    data = scio.loadmat(dataFile)
    mask = data['groundTruth']
    mask_8bit = cv2.normalize(mask[0][0][0].astype(np.float32), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    cv2.imwrite(os.path.join(dst_dir, file_name.split('.')[0] + '.png'), mask_8bit)
