# Use an official Python runtime as a parent image
FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install requests
RUN pip install psutil
#ENV NAME World
CMD ["python", "app.py"]
