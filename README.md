# 项目使用说明

## 项目重要文件说明

1. `static` 和 `templates`
   存放静态文件和网页
2. `Dockerfile` 和 `docker-compose.yml`
   docker部署文件
3. `requirement.txt`
   项目环境依赖
4. `modelWeb/DLModel/fast_text_model`
   存放模型的目录
5. `modelWeb/utils/dataHandle.py`
   数据预处理
6. `modelWeb/utils/train.py`
  训练脚本
7. `Sampledata,txt`
  样本数据

**目录结构**
```
.
├── DLModel
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── admin.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── fast_text_model
│   │   └── testModel.ftz
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Dockerfile
├── README.md
├── db.sqlite3
├── docker-compose.yml
├── manage.py
├── modelWeb
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pip.conf
├── requirements.txt
├── static
│   ├── css
│   │   ├── product.css
│   │   └── search.css
│   └── images
│       ├── 01.jpg
│       ├── 02.jpg
│       └── type.png
|__ Sampledata.txt
├── templates
│   └── show.html
└── utils
    ├── dataHandle.py
    └── train.py

12 directories, 40 files

```



## 初步使用
1. 在终端项目根目录下运行下面命令
```bash
python manager.py runserver
```
2. 待项目运行成功后，浏览器访问127.0.0.1:8000
3. 或者你想本地先部署一下
```bash
docker-compose build
docker-compose up
```

注意：若仅用`testModel.ftz`效果并不好，请根据下面说明根据自己需求训练一个模型
   
## 训练模型
根据实际数据集处理，相关训练使用请参考[Fasttext Github](https://github.com/facebookresearch/fastText/)

1. 处理数据
   请注意fasttext训练数据标签前缀`__label__`
2. 训练模型
   请根据文档调仓，训练出自己的模型。若模型较大，可以使用fasttext提供的压缩函数。

## 部署说明
1. 原始项目部署
   ```bash
   docker-compose build
   docker-compose up
   ```
2. 自定义模型请重新部署
   1. 只需更换模型路径（在`modelWeb/DLModel/views.py`）
   2. 运行
    ```bash
    docker-compose build
    docker-compose up
    ```
    3. 部署成功后访问`127.0.0.1:8000`即可

