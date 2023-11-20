import json
import os
import numpy as np
from PIL import Image
from labelme import utils
import shutil

# 将BSData的json格式的mask转换为png格式

def json2mask_multi(json_path, save_path, img_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for json_name in os.listdir(json_path):
        data = json.load(open(os.path.join(json_path, json_name)))
        json_name = json_name.split('.')[0]
        image_path = data['imagePath']
        _img_path = os.path.join(img_path, image_path)
        # 根据imageData字段的字符可以得到原图像
        img = utils.img_b64_to_arr(data['imageData'])
        # lbl为label图像（用类别名对应的数字来标，背景为0）
        # lbl_names为label名和数字的对应关系字典
        lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])
        # print(lbl_names)
        mask = Image.fromarray(lbl).convert('L')
        # putpalette给对象加上调色板，相当于上色：R,G,B
        # 三个数一组，对应于RGB通道，可以自己定义标签颜色
        mask.putpalette([0, 0, 0,
                         255, 255, 255,
                         255, 255, 0,
                         128, 128, 128])
        mask.save(os.path.join(save_path, 'BSData_' + json_name + "_mask.png"))
        shutil.copy(_img_path, os.path.join(save_path, 'BSData_' + json_name + ".png"))


json_path = r"E:\defect_datasets\datasets\seg\BSData-main\label"
save_path = r'E:\defect_datasets\datasets\seg\BSData-main\dataset_reg'
img_path = r'E:\defect_datasets\datasets\seg\BSData-main\data'
json2mask_multi(json_path, save_path, img_path)
