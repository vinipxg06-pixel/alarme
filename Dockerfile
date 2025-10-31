# Usar a imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o script Python e o arquivo de áudio para dentro do contêiner
COPY alarme.py /app/alarme.py
COPY sirene.mp3 /app/sirene.mp3

# Instalar dependências necessárias para tocar o som
RUN pip install pygame

# Comando para rodar o script Python
CMD ["python", "alarme.py"]
