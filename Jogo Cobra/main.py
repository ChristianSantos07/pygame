import pygame
from pygame.locals import *
from sys import exit
from random import randint

class run():
    def __init__(self, altura, largura):
        self.pg = pygame
        self.pg.init()
        self.altura = altura
        self.largura = largura
        self.tela = None
        self.eixo_x_maca = 0
        self.eixo_y_maca = 0
        self.eixo_x_cobra = 0
        self.eixo_y_cobra = 0
        self.x_controle = 0
        self.y_controle = 0
        self.pontos = 0
        self.lista_cabeca = []
        self.lista_corpo = []
        self.fonte = None
        self.comprimento_combra = 1
        self.musica_fundo = None
        self.som_colisao = None
        self.msg_pontos = ''
        self.clock = self.pg.time.Clock()

    def configure(self):
        self.pg.display.set_caption('Jogo')
        self.tela = self.pg.display.set_mode((self.largura, self.altura))
        self.clock.tick(10)
        self.eixo_x_cobra = self.largura / 2
        self.eixo_y_cobra = self.altura / 2
        self.x_controle = 20
        self.y_controle = 20
        self.fonte = self.pg.font.SysFont('arial', 40, True, True)
        self.pg.mixer.music.set_volume(0.1)
        self.musica_fundo = self.pg.mixer.music.load('./Jogo Cobra/fundo.mp3')
        self.som_colisao = self.pg.mixer.Sound('./Jogo Cobra/bipe.wav')
        self.pg.mixer.music.play(-1)
        self.zera_tela()
        self.sorteia_local_maca()
        self.atualiza_cabeca()
        self.atualiza_pontos()
        

    def show(self):
        while True:
            self.seta_clock(10)
            self.atualiza_pontos()
            #self.event()
              
            self.eixo_x_cobra += self.x_controle
            self.eixo_y_cobra += self.y_controle 

            cobra = self.pg.draw.rect(self.tela,  (0, 255, 0), (self.eixo_x_cobra, self.eixo_y_cobra, 20, 20))
            maca = self.pg.draw.rect(self.tela,  (255, 0, 0), (self.eixo_x_maca, self.eixo_y_maca, 20, 20))


            self.colide(cobra=cobra, maca=maca)
        
            self.tela.blit(self.msg_pontos, (400, 10))
            self.atualiza_cabeca()
            self.aumenta_cobra()
            self.pg.display.update()

    def atualiza_cabeca(self):
            self.lista_cabeca = []
            self.lista_cabeca.append(self.eixo_x_cobra)
            self.lista_cabeca.append(self.eixo_y_cobra)
            self.lista_corpo.append(self.lista_cabeca)

    def aumenta_cobra(self):
        for posicao in self.lista_corpo:
            self.pg.draw.rect(self.tela, (0,255,0), (posicao[0], posicao[1], 20, 20))
        if len(self.lista_corpo) > self.comprimento_combra:
             del self.lista_corpo[0]

    def atualiza_pontos(self):
        try:
            self.msg_pontos = self.fonte.render(f'Pontos: {self.pontos}', False, (0,0,0))
        except:
            self.msg_pontos = self.fonte.render(f'Pontos: 0', False, (0,0,0))
        

    def sorteia_local_maca(self):
        self.eixo_x_maca = randint(40, (self.largura - 40))
        self.eixo_y_maca = randint(50, (self.altura - 50))

    def quit(self):
        self.pg.quit()
        exit()

    def zera_tela(self):
        self.tela.fill((255,255,255))

    def apertou_tecla(self, ev):
        self.zera_tela()

        if ev == K_a:
            self.x_controle = -20
            self.y_controle = 0
        if ev == K_d:
           self.x_controle = 20
           self.y_controle = 0
        if ev == K_w:
            self.y_controle = -20
            self.x_controle = 0
        if ev == K_s:
           self.x_controle = 0
           self.y_controle = 20

        #self.verifica_altura_largura()
    
    # def verifica_altura_largura(self):
    #     if self.eixo_y_cobra >= self.altura or self.eixo_y_cobra < 0:
    #         self.eixo_y_cobra = self.eixo_y_cobra % self.altura

    #     if self.eixo_x_cobra >= self.largura or self.eixo_x_cobra < 0:
    #         self.eixo_x_cobra = self.eixo_x_cobra % self.largura


    def presionar_tecla(self):

        keys = self.pg.key.get_pressed()
        self.zera_tela()

        if keys[K_w]:
            self.eixo_y_cobra -= 20
        if keys[K_a]:
            self.eixo_x_cobra -= 20
        if keys[K_s]:
            self.eixo_y_cobra += 20
        if keys[K_d]:
            self.eixo_x_cobra += 20
        
        #self.verifica_altura_largura()

    def event(self):
        for event in self.pg.event.get():
            if event.type == QUIT:
                self.quit()
            
            elif event.type == KEYDOWN:
                self.apertou_tecla(ev=event.key)

        # Se precionar as teclas
        #self.presionar_tecla()
        
    def seta_clock(self, time):
        try:
            self.clock.tick(time)
        except:
            self.clock.tick(30)

    def colide(self, cobra, maca):
        if cobra.colliderect(maca):
            self.som_colisao.play()
            self.sorteia_local_maca()
            self.pontos += 1
            self.comprimento_combra += 1
            self.pg.display.update()
    

if __name__ == '__main__':
    jogo = run(altura=480, largura=640)
    jogo.configure()
    jogo.show()
    

    



