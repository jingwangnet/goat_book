FROM node:slim AS frontend
COPY src /src
WORKDIR /src/lists/static
RUN npm install -y

FROM python:slim AS backend
EXPOSE 8888
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
ENV DJANGO_DEBUG_FALSE=1
ENV DJANGO_SECRET_KEY=serit
ENV DJANGO_ALLOWED_HOST=superlists.jingwang.me
ENV DJANGO_CSRF_TRUSTED_ORIGIN=https://superlists.jingwang.me

WORKDIR /src

COPY --from=frontend /src /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

CMD gunicorn --bind :8888 superlists.wsgi
