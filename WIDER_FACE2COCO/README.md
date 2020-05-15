将WIDER_FACE数据标签转化为COCO数据集

- Training annotation

  ```bash
  python wider_to_coco.py wider_face_split/wider_face_train_bbx_gt.txt WIDER_train/images train.json
  ```

- Validation annotation

  ```bash
  python wider_to_coco.py wider_face_split/wider_face_val_bbx_gt.txt WIDER_val/images val.json
  ```



应用实例：

1.intel训练目标检测模型仓库[openvino_training_extensions](https://github.com/opencv/openvino_training_extensions)中人脸检测[face_detection.md](https://github.com/opencv/openvino_training_extensions/blob/develop/pytorch_toolkit/object_detection/face_detection.md)

