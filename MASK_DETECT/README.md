# **世界人工智能创新大赛-菁英挑战赛** ---口罩检测

官网：https://cvmart.net/race/7/base



方案1：

使用[OpenVINO™ Training Extensions](https://github.com/opencv/openvino_training_extensions.git)

克隆相关工程：

```
git clone https://gitee.com/ybli_code/openvino_training_extensions.git
cd openvino_training_extensions
cd pytorch_toolkit/object_detection/
git submodule update --init ../external/mmdetection
```

（新机器，可选）下载，安装[anaconda](https://www.anaconda.com/products/individual#macos)：

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
bash Anaconda3-2020.02-Linux-x86_64.sh
source ~/.bashrc
```

（新机器，可选）下载，安装[cuda](https://developer.nvidia.com/cuda-toolkit-archive),非root可不安装显卡驱动，保证原有驱动兼容即可

```
wget https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux -c
bash cuda_10.0.130_410.48_linux
vim ~/.bashrc
	export PATH=$PATH:/DATA/ybli/cuda-10.0/bin
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/DATA/cuda10.0/lib64
source ~/.bashrc
```

创建conda虚拟环境：

```
conda create -n mmdetecton python=3.7
conda activate mmdetecton
```

（新机器，可选）pip换源：

```
mkdir ~/.pip
vim ~/.pip/pip.conf
	[global]
	index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

由于国内使用conda速度较慢，pytorch更换源也效果不佳，一些大的包离线下载，采用pip安装：

离线下载安装[pytorch&torchvision](https://download.pytorch.org/whl/torch_stable.html)，根据cuda,python,系统,工程需求选择合适的版本。

```
wget https://download.pytorch.org/whl/cu100/torch-1.4.0%2Bcu100-cp37-cp37m-linux_x86_64.whl -c
wget https://download.pytorch.org/whl/cu100/torchvision-0.5.0%2Bcu100-cp37-cp37m-linux_x86_64.whl -c
pip install ./torch-1.4.0+cu100-cp37-cp37m-linux_x86_64.whl
pip install ./torchvision-0.5.0+cu100-cp37-cp37m-linux_x86_64.whl
```

安装mmdetection依赖：

```
pip install Cython
pip install -r requirements.txt
```

编译安装mmdetection：

```
cd ../../external/mmdetection/
python setup.py develop
```

口罩检测任务，直接想到复用人脸检测算法，分析人脸识别模型性能/速度：

| Model Name                                   | Complexity (GFLOPs) | Size (Mp) | AP for faces > 64x64 | [WiderFace](http://shuoyang1213.me/WIDERFACE/WiderFace_Results.html)(Easy/Medium/Hard) | Links                                                        | GPU_NUM |
| -------------------------------------------- | ------------------- | --------- | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------- |
| face-detection-retail-0005                   | 0.982               | 1.021     | 84.52%               | 78.97% / 70.80% / 37.32%                                     | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/wider_face_tiny_ssd_075x_epoch_70.pth), [configuration file](./configs/face-detection-retail-0005.py) | 2       |
| face-detection-0100                          | 0.785               | 1.828     | 86.16%               | 82.50% / 75.77% / 40.83%                                     | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/face-detection-0100.pth), [configuration file](./configs/face-detection-0100.py) | 2       |
| face-detection-0102                          | 1.767               | 1.842     | 91.47%               | 88.90% / 83.51% / 49.58%                                     | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/face-detection-0102.pth), [configuration file](./configs/face-detection-0102.py) | 2       |
| face-detection-0104                          | 2.405               | 1.851     | 92.69%               | 90.15% / 84.80% / 51.61%                                     | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/face-detection-0104.pth), [configuration file](./configs/face-detection-0104.py) | 4       |
| **face-detection-0105**                      | 2.853               | 2.392     | 93.34%               | 91.61% / 85.94% / 52.93%                                     | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/face-detection-0105.pth), [configuration file](./configs/face-detection-0105.py) | 4       |
| face-detection-0106                          | 339.597             | 69.920    | 94.49%               | 94.51% / 93.20% / 83.09%                                     | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/face-detection-0106.pth), [configuration file](./configs/face-detection-0106.py) | 8       |
| person-vehicle-bike-detection-crossroad-1016 | 3.560               | 2.887     | 62.55%               |                                                              | [snapshot](https://download.01.org/opencv/openvino_training_extensions/models/object_detection/person_vehicle_bike_sd512_mb2_clustered_epoch_21.pth), [configuration file](./configs/person-vehicle-bike-detection-crossroad-1016.py) |         |

Openvino模型：

| Model Name                                                   | Complexity (GFLOPs) | Size (Mp) | Face | Person | Vehicle | Bike | License plate | Product |
| ------------------------------------------------------------ | ------------------- | --------- | ---- | ------ | ------- | ---- | ------------- | ------- |
| [face-detection-retail-0005](./face-detection-retail-0005/description/face-detection-retail-0005.md) | 0.982               | 1.021     | X    |        |         |      |               |         |
| [face-detection-0100](./face-detection-0100/description/face-detection-0100.md) | 0.785               | 1.828     | X    |        |         |      |               |         |
| [face-detection-0102](./face-detection-0102/description/face-detection-0102.md) | 1.767               | 1.842     | X    |        |         |      |               |         |
| [face-detection-0104](./face-detection-0104/description/face-detection-0104.md) | 2.405               | 1.851     | X    |        |         |      |               |         |
| [face-detection-0105](./face-detection-0105/description/face-detection-0105.md) | 2.853               | 2.392     | X    |        |         |      |               |         |
| [face-detection-0106](./face-detection-0106/description/face-detection-0106.md) | 339.597             | 69.920    | X    |        |         |      |               |         |
| [person-vehicle-bike-detection-crossroad-1016](./person-vehicle-bike-detection-crossroad-1016/description/person-vehicle-bike-detection-crossroad-1016.md) | 3.560               | 2.887     |      | X      | X       | X    |               |         |
| [vehicle-license-plate-detection-barrier-0106](./vehicle-license-plate-detection-barrier-0106/description/vehicle-license-plate-detection-barrier-0106.md) | 0.349               | 0.634     |      |        | X       |      | X             |         |

赛题最低要求：若参赛者成绩，F1-Score<0.5，算法所得性能值FPS<5，则该比赛成绩无法进入获奖评选。兼顾速度与准确率，选用face-detection-0105

赛题使用的数据集标注格式为VOC，可参照行人车辆检测[configuration file](https://github.com/opencv/openvino_training_extensions/blob/develop/pytorch_toolkit/object_detection/configs/person-vehicle-bike-detection-crossroad-1016.py)文件以及人脸检测[configuration file](https://github.com/opencv/openvino_training_extensions/blob/develop/pytorch_toolkit/object_detection/configs/face-detection-0105.py)文件，建立口罩检测的配置文件。

http://10.9.0.146:8888/group1/M00/00/01/CgkA617CSSKEUZr9AAAAAJtA_fg1825.gz

