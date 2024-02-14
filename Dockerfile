FROM node:slim AS frontend
COPY src /src
WORKDIR /src/lists/static
RUN npm install -y

FROM python:slim AS backend
EXPOSE 8888
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

WORKDIR /src

COPY --from=frontend /src /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8888
