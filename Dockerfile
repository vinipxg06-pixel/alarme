# Usar a imagem oficial do Python com suporte para arm64 como base
FROM --platform=linux/arm64 python:3.9-slim

# Instalar dependências de áudio e compilação para o pygame
RUN apt-get update && apt-get install -y \
    gcc \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libfreetype6-dev \
    libportmidi-dev \
    pkg-config \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o script Python e o arquivo de áudio para dentro do contêiner
COPY alarme.py /app/alarme.py
COPY sirene.mp3 /app/sirene.mp3

# Instalar a biblioteca pygame necessária para tocar o som
RUN pip install pygame

# Comando para rodar o script Python
CMD ["python", "alarme.py"]
