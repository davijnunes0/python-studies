FROM python:3.11-slim AS builder

WORKDIR /app

# Copia os arquivos e a pasta para o diretório de trabalho atual (.) que é /app
COPY run.py .
COPY __init__.py .
COPY src/ ./src/

# Comando para executar o script
CMD ["python", "run.py"]