FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

RUN groupadd --gid 1000 app \
    && useradd --uid 1000 -d /home/app -M --shell /sbin/nologin --gid app app \
    && pip install --upgrade pip \
    && python -m venv /venv

# Copy the requirements file explicitly
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN /venv/bin/pip install -r /app/requirements.txt

ENV PATH=/venv/bin:${PATH}

# WORKDIR /app

# ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]




