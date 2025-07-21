# Use imagem base Python
FROM python:3.9-slim  

# Diretório de trabalho
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependências
RUN pip install -r requirements.txt

# Copiar código
COPY app.py .

# Copiar dados do Titanic
COPY titanic-project/data/ ./data/

# Comando para executar
CMD ["python", "app.py"]