FROM python:slim
EXPOSE 8888
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src /src
WORKDIR /src
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8888
