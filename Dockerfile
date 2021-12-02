FROM python:3.8

ENTRYPOINT ["python", "./bionic_eye_device_docker_version.py"]

ADD requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app

ADD bionic_eye_device_docker_version.py /

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./bionic_eye_device_docker_version.py" ]
