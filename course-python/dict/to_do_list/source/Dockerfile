FROM python:3.11-alpine

# Instalar compiladores e dependências de build
RUN apk add --no-cache build-base libffi-dev

# Instalar pacotes Python populares
RUN pip install --no-cache-dir numpy pandas requests

CMD ["python"]