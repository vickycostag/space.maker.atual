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
dadosSalvos = False
fundo = pygame.image.load("fundo.jpg")
caixaTexto = pygame.image.load("f10.png")
caixaSalvos = pygame.image.load("caixa salvos.png")
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            cordenadas.append(pos)
            nome = simpledialog.askstring("Space", "O nome dessa estrela será: ")
            if nome is None or nome.strip() == "":
                nome = "desconhecida"
                print(nome)
                nomes.append(nome)
            if nome != "":
                print(nome)
                nomes.append(nome)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F10:
                cordenadas = []
                nomes = []
                linhas = []
                pygame.display.update()
            if event.key == pygame.K_F11:
                dadosSalvos = True
                
    if dadosSalvos:
        biblioDados = {'estrelas': nomes }
        biblioCord = {'cordenadas': cordenadas}
        salvando.append(biblioDados)
        salvando.append(biblioCord)
        for dados in salvando:
            pygame.font.init()
            tela.blit(caixaSalvos, (20, 70))
            textoDados = fontepadrao.render(str(biblioDados), 1, preto)
            textoCord = fontepadrao.render(str(biblioCord), 1, preto)
            tela.blit(textoDados, (50, 110))
            tela.blit(textoCord, (50, 135))
            pygame.display.update()
            time.sleep(2)
        dadosSalvos = False
        
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


