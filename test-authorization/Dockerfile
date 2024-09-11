FROM python:latest

RUN pip install requests 

WORKDIR /usr/app/src
ENV LOG=1
RUN mkdir log
COPY authorization.py ./

CMD [ "python" , "./authorization.py" ]