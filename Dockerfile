FROM python:3
ADD ftapp.py /
CMD [ "python3", "./ftapp.py" ]
