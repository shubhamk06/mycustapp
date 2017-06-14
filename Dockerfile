FROM python:3
ADD aa.py /
ADD bb.py /
CMD [ "python", "./aa.py" ]
