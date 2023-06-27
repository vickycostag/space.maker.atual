# importações
import pygame
import time
import random
from tkinter import simpledialog

# coisas do game
pygame.init()
tamanho = (1024, 683)
tamanhoCaixa = (-100, -90)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
cor = (255, 255, 255)
preto = (0,0,0)
fonte = pygame.font.get_default_font()
fontepadrao = pygame.font.SysFont(fonte, 30)
raio = 5
running = True

# listas
cordenadas = []
nomes = []
linhas = []  
salvando = []


# música, ícone, nome...
fundo = pygame.image.load("fundo.jpg")
caixaTexto = pygame.image.load("f10.png")
caixaSalvos = pygame.image.load("salvos.png")
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)
icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("this is SPACE MAKER!")

# dando início ao game
while running:
    tela.blit(fundo, (0, 0))
    tela.blit(caixaTexto, (tamanhoCaixa))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            cordenadas.append(pos)
            nome = simpledialog.askstring("Space", "O nome dessa estrela será: ")
            if nome != "":
                print(nome)
                nomes.append(nome)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F10:
                cordenadas = []
                nomes = []
                linhas = []
                pygame.display.update()
                    
                
    #para desenhar as estrelinhas e escrever os nomes
    for i in range(len(cordenadas)):
        pygame.draw.circle(tela, cor, cordenadas[i], raio)
        pygame.font.init()
        texto = fontepadrao.render(nomes[i], 1, cor)
        tela.blit(texto, cordenadas[i])

    #para desenhar as linhas
    for linha in linhas:
        pygame.draw.line(tela, cor, linha[0], linha[1]) 

    if len(cordenadas):
        for i in range(len(cordenadas) - 1):
            linhas.append([cordenadas[i], cordenadas[i + 1]])  

    pygame.display.update()
    clock.tick(60)

pygame.quit()


