FROM python:3.9


ENV PYHTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/construction

#RUN rm -rf /usr/src/construction
COPY ./requirements.txt /usr/src/construction/requirements.txt
#COPY .env /usr/src/construction/.env # xato

RUN pip install -r /usr/src/construction/requirements.txt

COPY . /usr/src/construction


EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
