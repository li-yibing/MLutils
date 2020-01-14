import hashlib
import os
import cv2
import numpy as np
from skimage.measure import compare_ssim


def remove_same_piture_by_get_md5(path):
    img_list = os.listdir(path)
    print(img_list)
    md5_list =[]
    for filename in img_list:
        m = hashlib.md5()
        mfile = open(os.path.join(path,filename), "rb")
        m.update(mfile.read())
        mfile.close()
        md5_value = m.hexdigest()
        #print(md5_value)
        if (md5_value in md5_list):
            os.remove(os.path.join(path,filename))
        else:
            md5_list.append(md5_value)
            print('total %s images'%len(md5_list))
            
def remove_simillar_picture_by_perception_hash(path):
    img_list = os.listdir(path)
    hash_dic = {}
    hash_list = []
    count_num = 0
    for img_name in img_list:
        try:
            img = cv2.imread(os.path.join(path, img_name))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            count_num+=1
            print(count_num)
        except:
            continue

        img = cv2.resize(img,(8,8))

        avg_np = np.mean(img)
        img = np.where(img>avg_np,1,0)
        hash_dic[img_name] = img
        if len(hash_list)<1:
            hash_list.append(img)
        else:
            for i in hash_list:
                flag = True
                dis = np.bitwise_xor(i,img)

                if np.sum(dis) < 5:
                    flag = False
                    os.remove(os.path.join(path, img_name))
                    break
            if flag:
                hash_list.append(img)

def remove_simillar_image_by_ssim(path):
    img_list = os.listdir(path)
    img_list.sort()
    hash_dic = {}
    save_list = []
    count_num = 0
    for i in range(len(img_list)):
        try:
            img = cv2.imread(os.path.join(path, img_list[i]))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (256, 256))
            count_num += 1
            print(count_num)
        except:
            continue
        if count_num == 1:
            save_list.append(img_list[i])
            continue
        elif len(save_list) <5:
            flag = True
            for j in range(len(save_list)):
                com_img = cv2.imread(os.path.join(path,save_list[j]))
                com_img = cv2.cvtColor(com_img,cv2.COLOR_BGR2GRAY)
                com_img = cv2.resize(com_img,(256,256))
                sim = compare_ssim(img, com_img)
                if sim > 0.4:
                    os.remove(os.path.join(path,img_list[i]))
                    flag = False
                    break
            if flag:
                save_list.append(img_list[i])
        else:
            for save_img in save_list[-5:]:
                com_img = cv2.imread(os.path.join(path,save_img))
                com_img = cv2.cvtColor(com_img, cv2.COLOR_BGR2GRAY)
                com_img = cv2.resize(com_img, (256, 256))
                sim = compare_ssim(img, com_img)
                if sim > 0.4:
                    os.remove(os.path.join(path, img_list[i]))
                    flag = False
                    break
            if flag:
                save_list.append(img_list[i])


if __name__ == "__main__":

    img_path = '/home/ybli/ybli/nuaa/dataset/test/real/'
    #remove_same_piture_by_get_md5(img_path)
    #remove_simillar_picture_by_perception_hash(img_path)
    remove_simillar_image_by_ssim(img_path)