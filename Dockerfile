# Imagem base enxuta com Python 3.11
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os requisitos primeiro para melhor cache no build
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . .

# Garante que logs sejam enviados diretamente ao terminal
ENV PYTHONUNBUFFERED=1

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]
