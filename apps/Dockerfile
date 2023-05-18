FROM python:3.9


ENV PYHTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/construction

COPY ../requirements/requirements.txt /usr/src/construction/requirements/requirements.txt

RUN pip install -r /usr/src/construction/requirements/requirements.txt

COPY .. /usr/src/construction

EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "collectstatic"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


