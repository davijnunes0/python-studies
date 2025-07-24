# --- ESTÁGIO 1: O "Builder" ---
# Usamos uma imagem completa para garantir que todas as ferramentas de compilação
# estejam disponíveis, caso alguma biblioteca em requirements.txt precise delas.
FROM python:3.11 AS builder

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências em um local isolado dentro do builder
# Usar --no-cache-dir ajuda a manter a camada menor
RUN pip install --no-cache-dir --upgrade pip
COPY src/requirements.txt .
RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt


# --- ESTÁGIO 2: A Imagem Final (Produção) ---
# Começamos de novo com uma imagem base limpa e super leve.
FROM python:3.11-slim

# Cria um usuário não-root para rodar a aplicação (Melhor prática de segurança)
RUN adduser --system --group --no-create-home appuser
USER appuser

# Define o diretório de trabalho para o usuário não-root
WORKDIR /home/appuser/app

# Copia as dependências que foram instaladas no estágio 'builder'
# Esta é a "mágica" do multi-stage build!
COPY --from=builder /install /usr/local

# Copia o código-fonte da aplicação
# Usar "COPY . ." aqui é mais limpo, assumindo que você tem um .dockerignore
COPY --chown=appuser:appuser . .

# Comando para executar a aplicação
CMD ["python", "run.py"]