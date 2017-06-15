FROM python:3
WORKDIR /usr/src/app
ADD ftapp.py .
RUN chmod 777 /usr/src/app/
CMD [ "python", "ftapp.py" ]
