FROM python:3.10

WORKDIR /myapp

COPY . .

RUN pip install mysql-connector-python 
RUN pip install termcolor 

CMD [ "python", "main.py" ]

