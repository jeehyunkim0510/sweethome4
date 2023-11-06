FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/jeehyunkim0510/sweethome4.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn","sweethome4", "--bind", "0.0.0.0:8000"]