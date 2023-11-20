import os
import numpy as np
from tqdm import trange
import shutil

"""
计算miou并将iou阈值高低移动到对应文件夹
"""


# 文件夹路径


# 遍历文件夹中的文件

def calculate_and_move_mask(target_path, reg_path, high_iou_path,low_iou_path):
    iou_list_32 = []
    iou_list_8 = []
    iou_list_64 = []
    iou_list_128 = []
    for i in trange(len(os.listdir(target_path))):
        # 文件名
        file_name = os.listdir(target_path)[i]
        if 'everything_8' in file_name:
            # 提取数字部分
            number = file_name.split('_')[-1][:-4]
            iou_list_8.append(float(number))
            if float(number) < 0.01:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), low_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), low_iou_path)
            elif float(number) > 0.95:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), high_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), high_iou_path)
            else:
                pass
        elif 'everything_32' in file_name:
            # 提取数字部分
            number = file_name.split('_')[-1][:-4]
            iou_list_32.append(float(number))
            if float(number) < 0.01:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), low_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), low_iou_path)
            elif float(number) > 0.95:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), high_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), high_iou_path)
            else:
                pass
        elif 'everything_64' in file_name:
            # 提取数字部分
            number = file_name.split('_')[-1][:-4]
            iou_list_64.append(float(number))
            if float(number) < 0.01:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), low_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), low_iou_path)
            elif float(number) > 0.95:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), high_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), high_iou_path)
            else:
                pass
        elif 'everything_128' in file_name:
            # 提取数字部分
            number = file_name.split('_')[-1][:-4]
            iou_list_128.append(float(number))
            if float(number) < 0.01:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), low_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), low_iou_path)
            elif float(number) > 0.95:
                prefix = '_'.join(file_name.split('_')[:-4])
                for file_prefix in os.listdir(target_path):
                    if prefix in file_prefix:
                        shutil.copy(os.path.join(target_path, file_prefix), high_iou_path)
                for file_prefix_reg in os.listdir(reg_path):
                    if prefix in file_prefix_reg:
                        shutil.copy(os.path.join(reg_path, file_prefix_reg), high_iou_path)
            else:
                pass
        else:
            pass
    # mean
    print('32:', np.mean(iou_list_32))
    print('8:', np.mean(iou_list_8))
    print('64:', np.mean(iou_list_64))
    print('128:', np.mean(iou_list_128))


def mask_move_point_bbox(target_path, reg_path, high_iou_path, low_iou_path):
    # 遍历文件夹中的文件
    for i in trange(len(os.listdir(target_path))):
        # 文件名
        file_name = os.listdir(target_path)[i]
            # 提取iou
        number = file_name.split('_')[-1][:-4]
        if 'bbox' in file_name:
            prefix = '_'.join(file_name.split('_')[:-5])
        else:
            prefix = '_'.join(file_name.split('_')[:-4])
        # iou_list_8.append(float(number))
        if float(number) < 0.01:
            # prefix = '_'.join(file_name.split('_')[:-4])
            shutil.copy(os.path.join(target_path, file_name),
                        low_iou_path)
            for file_prefix_reg in os.listdir(reg_path):
                if prefix in file_prefix_reg:
                    shutil.copy(os.path.join(reg_path, file_prefix_reg),
                                low_iou_path)
        elif float(number) > 0.95:
            # prefix = '_'.join(file_name.split('_')[:-4])
            shutil.copy(os.path.join(target_path, file_name),
                        high_iou_path)
            for file_prefix_reg in os.listdir(reg_path):
                if prefix in file_prefix_reg:
                    shutil.copy(os.path.join(reg_path, file_prefix_reg),
                                high_iou_path)
        else:
            pass


def check_exits_folder(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)


if __name__ == '__main__':
    root_path = r'E:\defect_datasets\datasets\sam_dataset\test\datasets_all'
    # target_path = r"E:\defect_datasets\datasets\sam_dataset\test\other\everything_vit_b"
    # reg_path = r'E:\defect_datasets\datasets\sam_dataset\test\other\dataset_reg_other'
    # high_iou_path = r'E:\defect_datasets\datasets\sam_dataset\test\other\everything_vit_b_high_iou'
    # low_iou_path = r'E:\defect_datasets\datasets\sam_dataset\test\other\everything_vit_b_low_iou'
    # dataset_lists = ['AITEX', 'BSData', 'CrackForest', 'KSDD', 'MTD', 'RSDDs']
    dataset_folder_lists = ['dataset_reg', 'everything_vit_b', 'everything_vit_b_high_iou', 'everything_vit_b_low_iou',
                            'everything_vit_h', 'everything_vit_h_high_iou', 'everything_vit_h_low_iou',
                            'point_bbox_vit_b', 'point_bbox_vit_b_high_iou', 'point_bbox_vit_b_low_iou']
    # for dataset in dataset_lists:
    #     dataset_reg_path = os.path.join(root_path, dataset, dataset_folder_lists[0])
    # # move datasets_all
    # for root, dirs, files in os.walk(r'E:\defect_datasets\datasets\sam_dataset\test\other'):
    #     for file in files:
    #         for dataset in dataset_lists:
    #             if dataset in file:
    #                 prefix = root.split('\\')[-1]
    #                 move_path = os.path.join(root_path, dataset, prefix)
    #                 check_exits_folder(move_path)
    #                 shutil.move(os.path.join(root, file), move_path)
    for dataset_name in os.listdir(root_path):
        print(dataset_name)
        reg_path = os.path.join(root_path, dataset_name, dataset_folder_lists[0])
        for i in [1, 4]:
            print(dataset_folder_lists[i])
            target_path = os.path.join(root_path, dataset_name, dataset_folder_lists[i])
            high_iou_path = os.path.join(root_path, dataset_name, dataset_folder_lists[i + 1])
            low_iou_path = os.path.join(root_path, dataset_name, dataset_folder_lists[i + 2])
            check_exits_folder(high_iou_path)
            check_exits_folder(low_iou_path)
            calculate_and_move_mask(target_path, reg_path, high_iou_path, low_iou_path)
        target_path = os.path.join(root_path, dataset_name, dataset_folder_lists[7])
        high_iou_path = os.path.join(root_path, dataset_name, dataset_folder_lists[8])
        low_iou_path = os.path.join(root_path, dataset_name, dataset_folder_lists[9])
        check_exits_folder(high_iou_path)
        check_exits_folder(low_iou_path)
        mask_move_point_bbox(target_path, reg_path, high_iou_path, low_iou_path)


