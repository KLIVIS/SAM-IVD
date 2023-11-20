import os
import cv2
import shutil

# 剔除mask无异常的图像和掩码

# 定义文件夹路径和掩码文件名后缀
folder_path = r"E:\defect_datasets\datasets\seg\dataset_reg_other\dataset_reg_other"
mask_suffix = "_mask.png"

# 遍历文件夹中的文件
for file_name in os.listdir(folder_path):
    # 如果文件是掩码文件
    if file_name.endswith(mask_suffix):
        # 构造掩码文件路径
        mask_path = os.path.join(folder_path, file_name)
        # 读取掩码文件
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        # 如果掩码图像全黑
        # print(mask.any())
        if not mask.any():
            # 输出文件名
            img_name = file_name.split('_mask')[0] + '.png'
            if os.path.exists(os.path.join(folder_path, img_name)):
                # 构造图像文件路径
                img_path = os.path.join(folder_path, img_name)
                # 删除图像文件
                os.remove(img_path)
                # 删除掩码文件
                os.remove(mask_path)
                # 输出文件名
                print(img_name)
                print(mask_path)
                print('----------------------')
            elif os.path.exists(os.path.join(folder_path, file_name.split('_mask')[0] + '.jpg')):
                img_path = os.path.join(folder_path, file_name.split('_mask')[0] + '.jpg')
                os.remove(img_path)
                os.remove(mask_path)
                print(img_name)
                print(mask_path)
                print('----------------------')
            else:
                print(img_name)
                print(mask_path)
                raise Exception('no match the mask')



