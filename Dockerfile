FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/jeehyunkim0510/sweethome4.git

WORKDIR /home/sweethome4/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-6r197te%kyjj67&e%v%u=f1$g&7namir$u2&nr7a8+i89zrl3n" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]