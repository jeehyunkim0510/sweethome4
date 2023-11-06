FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/jeehyunkim0510/sweethome6.git

WORKDIR /home/sweethome6/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-#n3x1w7rx4yu=_8ujwr#!#(1ik-jqwtkd&qhjj6=px^7_u$g9e" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]