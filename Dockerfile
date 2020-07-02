# 从仓库拉取 带有 python 3.7 的 Linux 环境
FROM python:3.7.7-stretch

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 添加 Debian 清华镜像源
RUN echo \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\
  > /etc/apt/sources.list



# 创建 model文件夹并将其设置为工作目录
RUN mkdir /model
WORKDIR /model
# 更新 pip
RUN pip install pip -U
# 将 requirements.txt 复制到容器
ADD requirements.txt /model/
COPY pip.conf /etc/pip.conf
# 安装库
RUN pip install -r requirements.txt
# 将当前目录复制到容器
ADD . /model/