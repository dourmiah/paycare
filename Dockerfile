FROM python:3.9-slim
WORKDIR /home/app
COPY . .
RUN apt-get update
RUN apt-get install nano unzip
RUN apt-get install curl -y
RUN pip install -r requirements.txt
ENV PYTHONPATH=/home/app
CMD ["python", "etl.py"]