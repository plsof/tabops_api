FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code/
ADD tabops_api/requirements.txt /code/
#ADD tabops_api/ /code/
RUN pip install --upgrade pip && pip install  -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt