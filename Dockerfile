FROM python:3.8

ENTRYPOINT ["python", "./bionic_eye_device.py"]

ADD requirements.txt /

RUN pip install -r /requirements.txt

ADD bionic_eye_device.py /

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./bionic_eye_device.py" ]
