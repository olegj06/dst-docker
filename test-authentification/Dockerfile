FROM python:latest



RUN pip install requests 

WORKDIR /usr/app/src
ENV LOG=1
RUN mkdir log
COPY authentification.py ./

CMD [ "python" , "./authentification.py" ]