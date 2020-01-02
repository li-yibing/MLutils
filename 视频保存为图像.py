# -*- coding:utf-8 -*-
import cv2
import os


def video2img(video_path='./video.mp4', img_path='./img/', img_name='img'):
    '''
    :param video_path: 视频文件路径 默认：'./video.mp4'
    :param img_path: 保存图像路径（文件夹） 默认'./img/'
    :param img_name: 保存图像文件名前缀 默认'img'
    :return:
    '''
    vc = cv2.VideoCapture(video_path)  # 读入视频文件
    count = 0
    try:
        os.makedirs(img_path)
        print("make path")
    except:
        pass
    rval = vc.isOpened()

    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        # pic_path = folder_name+'/'
        if rval:
            count = count + 1
            num = ("%06d" % (count))
            # row, col, channel = frame.shape
            cv2.imwrite(img_path + img_name + str(num) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_图像名 数字.jpg
            # cv2.waitKey(1)
        else:
            break
    vc.release()
    print('save_success:' + str(num))



if __name__ == "__main__":

    # 测试视频转图像 video2img
    video_path = '/DATA/ybli/nuaa/video/real/Live_1203_01.mp4'
    img_path = './img/'
    img_name = 'Live'
    video2img(video_path, img_path, img_name)


