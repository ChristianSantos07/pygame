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
        self.x_azul = 0
        self.x_azul = 0
        self.x = 0
        self.y = 0
        self.pontos = 0
        self.fonte = None
        self.clock = self.pg.time.Clock()

    def configure(self):
        self.pg.display.set_caption('Jogo')
        self.tela = self.pg.display.set_mode((self.largura, self.altura))
        self.clock.tick(10)
        self.x = self.largura / 2
        self.y = self.altura / 2
        self.fonte = self.pg.font.SysFont('arial', 40, True, True)
        self.sorteia_local()

    def sorteia_local(self):
        self.x_azul = randint(40, (self.largura - 40))
        self.y_azul = randint(50, (self.altura - 50))

    def quit(self):
        self.pg.quit()
        exit()

    def zera_tela(self):
        self.tela.fill((0,0,0))

    def apertou_tecla(self, ev):
        self.zera_tela()

        if ev == K_a:
            self.x -= 20
        if ev == K_s:
           self.y += 20
        if ev == K_d:
           self.x += 20
        if ev == K_w:
            self.y -= 20
    
    def verifica_altura_largura(self):
        if self.y >= self.altura or self.y < 0:
            self.y = self.y % self.altura

        if self.x >= self.largura or self.x < 0:
            self.x = self.x % self.largura


    def presionar_tecla(self):
        self.seta_clock(20)

        keys = self.pg.key.get_pressed()
        self.zera_tela()

        if keys[K_w]:
            self.y -= 20
        if keys[K_a]:
            self.x -= 20
        if keys[K_s]:
            self.y += 20
        if keys[K_d]:
            self.x += 20
        
        self.verifica_altura_largura()

    def event(self):
        for event in self.pg.event.get():
            if event.type == QUIT:
                self.quit()
            
            
            
            # elif event.type == KEYDOWN:
            #     #self.apertou_tecla(ev=event.key)
            #     self.presionar_tecla()
        self.presionar_tecla()
        
    def seta_clock(self, time):
        try:
            self.clock.tick(time)
        except:
            self.clock.tick(30)

    def show(self):
        while True:
            mensagem = f'Pontos: {self.pontos}'
            texto_formatado = self.fonte.render(mensagem, False, (255,255,255))

            self.event()

            #self.movimentar_retangulo()
              
            ret_vermelho = self.pg.draw.rect(self.tela,  (255, 0, 0), (self.x, self.y, 40, 50))
            ret_azul = self.pg.draw.rect(self.tela,  (0, 0, 255), (self.x_azul, self.y_azul, 40, 50))

            self.colide(ret_vermelho=ret_vermelho, ret_azul=ret_azul)
            #pg.draw.circle(tela, (255, 0, 0), (300, 260), 40)
            #pg.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 2)
            self.tela.blit(texto_formatado, (400, 10))
            self.pg.display.update()

    def colide(self, ret_vermelho, ret_azul):
        if ret_vermelho.colliderect(ret_azul):
            self.sorteia_local()
            self.pontos += 1
    
    def movimentar_retangulo(self):
        self.tela.fill((0,0,0))
        self.clock.tick(50)

        self.pg.draw.rect(self.tela,  (0, 255, 0), (self.x, self.y, 40, 50))

        self.y += 1

        if self.y >= self.altura:
            self.y = 0

if __name__ == '__main__':
    jogo = run(altura=480, largura=640)
    jogo.configure()
    jogo.show()
    

    



