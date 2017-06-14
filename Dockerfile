FROM python:3
RUN pip install -r requirements.txt
ADD aa.py /
ADD bb.py /
CMD [ "python", "./aa.py" ]
