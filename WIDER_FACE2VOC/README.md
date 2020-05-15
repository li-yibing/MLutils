



# WIDER FACE PASCAL VOC ANNOTATIONS

convert.py将[WIDER FACE](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/) 标注格式转化为[Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) XML格式.

使用方法：

```
usage: convert.py [-h] [-ap ANNOTATIONS_PATH] [-tp TARGET_PATH]
                  [-ip IMAGES_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -ap ANNOTATIONS_PATH, --annotations-path ANNOTATIONS_PATH
                        the annotations file path.
                        ie:"./wider_face_split/wider_face_train_bbx_gt.txt".
  -tp TARGET_PATH, --target-path TARGET_PATH
                        the target directory path where XML files will be
                        copied.
  -ip IMAGES_PATH, --images-path IMAGES_PATH
                        the images directory path. ie:"./WIDER_train/images"
```

使用实例：

```
$ ./convert.py -ap ./wider_face_split/wider_face_train_bbx_gt.txt -tp ./WIDER_train_annotations/ -ip ./WIDER_train/images/
$ ./convert.py -ap ./wider_face_split/wider_face_val_bbx_gt.txt -tp ./WIDER_val_annotations/ -ip ./WIDER_val/images/
```

TODO:

WIDER_FACE标注文件没有人脸时，标注文件解析错误。现有方法： 在标注txt中搜索 0 0 0 0 0 0 0 0 0 0 更换上一条数据0-->1



generate.py将[Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) XML格式标签整理成txt列表

使用方法：

```
usage: generate.py [-h] [--input INPUT] [--output OUTPUT]

生成VOC标注文件列表

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        path to annotations
  --output OUTPUT, -o OUTPUT
                        path to txt list
```

使用实例：

```
python generate.py -i WIDER_train_annotations/ -o train.txt
python generate.py -i WIDER_val_annotations/ -o val.txt
```



应用实例：

1.[mmdetection](https://github.com/open-mmlab/mmdetection)中人脸检测的训练[README.md](https://github.com/open-mmlab/mmdetection/blob/v1.2.0/configs/wider_face/README.md)

