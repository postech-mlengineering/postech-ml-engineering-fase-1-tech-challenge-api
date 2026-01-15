FROM python:3.11-slim

WORKDIR /app

#instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry

#poetry instala libs diretamente no sistema
RUN poetry config virtualenvs.create false

#copia arquivos de dependência
COPY pyproject.toml poetry.lock ./

#instala dependências
RUN poetry install --without dev --no-interaction --no-ansi

#copia aplicação
COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 5000

CMD ["python", "app.py"]
