FROM python:3
ADD aa.py /
ADD bb.py /
RUN pip install os
CMD [ "python", "./aa.py" ]