FROM python:3
ADD ftapp.py /
RUN chmod 777 /usr/src/app
CMD [ "python3", "./ftapp.py" ]
