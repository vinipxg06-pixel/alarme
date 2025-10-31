import pygame
import time

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load("sirene.mp3")

# Reproduz o áudio em loop
pygame.mixer.music.play(-1)

# Deixa o som tocando por 30 segundos (você pode mudar esse tempo conforme necessário)
print("Alarme ativado! Tocando sirene...")
time.sleep(30)

# Para o som depois do tempo especificado
pygame.mixer.music.stop()
print("Alarme desativado!")
