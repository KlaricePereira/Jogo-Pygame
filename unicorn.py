import math
import random

import pygame
from pygame import mixer

#A classe Personagem é a classe pai e contém funções para movimentar e desenhar personagens, e também tem funções para obter as coordenadas x e y de um personagem.
class Personagem:  

    def __init__(self,x,y,mx,my ,s):
        self.perX = x  
        self.perY = y  
        self.perX_muda = mx
        self.perY_muda = my 
        self.scr=s 
        self.iPer = None
    
    def setMx(self,mx):  
        self.perX_muda = mx
    
    def setMy(self,my):  
        self.perY_muda = my
        
    def inverteMx(self):
        self.perX_muda = self.perX_muda * -1        
        
    def inverteMy(self):
        self.perY_muda = self.perY_muda * -1

    def movimentaXD(self):  
        self.perX += self.perX_muda
        
    def movimentaXE(self):  
        self.perX -= self.perX_muda

    def movimentaYB(self):  
        self.perY += self.perY_muda
        
    def movimentaYC(self):  
        self.perY -= self.perY_muda


    def desenha(self): 
        self.scr.blit(self.iPer, (self.perX,self.perY))
    
    def getX(self): 
        return self.perX
    
    def getY(self): 
        return self.perY
    
#A classe Unicornio herda da classe Personagem e é usada para criar o personagem principal do jogo. Ele tem a capacidade de mover-se para a direita e esquerda dentro da janela do jogo.
class Unicornio(Personagem):  

    def __init__(self,x,y,mx,s):
        super().__init__(x,y,mx,0,s)  
        self.iPer = pygame.image.load('player.png')  
        self.direcao = "d"
    
    def movimentaXD(self): 
        if (self.perX < 736):
            super().movimentaXD()
        
    def movimentaXE(self): 
        if (self.perX > 0):
            super().movimentaXE()
        

# classe Fantasma1 também herda da classe Personagem e é usada para criar um personagem
#inimigo que se move horizontalmente de um lado para o outro na janela do jogo. A classe
#Fantasma1 também contém funções para testar a colisão entre o personagem inimigo e as balas do jogador.
#Quando uma colisão é detectada, a pontuação do jogador aumenta e o personagem inimigo é reposicionado em uma nova posição aleatória.    
class Fantasma1 (Personagem):  
    
    def __init__(self,x,y,mx,my,s,j):
        super().__init__(x,y,mx,my,s)
        self.iPer = pygame.image.load('enemy1.png')        
        self.jogo=j   
        self.ponto=3
        self.direcao = "d"
        self.reposiciona()
    
    def movimenta(self): 
        if(self.direcao=="d"):
            self.movimentaXD()  
            if self.perX >= 736:
                self.direcao = "e"
                self.movimentaYB()
        if(self.direcao=="e"):
            self.movimentaXE()  
            if self.perX < 0:
                self.direcao = "d"
                self.movimentaYB()
                
    def reposiciona(self):
        self.perX = random.randint(0, 736)  
        self.perY = random.randint(50, 150) 
        
    def desenha(self):   
        b=self.jogo.getBala()  
       
        if(b!=None and b.getEstado()!="fim"):  
            colidiu=self.testaColisao(b) 
        else:
            colidiu=False
            
        if(colidiu==False):   
            self.movimenta()  
        else:  
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()  
            b.setEstado("fim")  
            self.jogo.addPlacar(self.ponto)  
            self.reposiciona()
        
        super().desenha()  
        
        
    def testaColisao(self,b):       
        distancia= math.sqrt(math.pow(self.perX - b.getX(), 2) + (math.pow(self.perY - b.getY(), 2)))
        if distancia < 27:
            return True
        else:
            return False
#A classe Fantasma2 também herda da classe Personagem e é usada para criar um segundo tipo de personagem inimigo que se move horizontalmente de um lado para o outro na janela do jogo. A classe Fantasma2 também contém funções para testar a colisão entre o personagem inimigo e as balas do jogador, e funciona da mesma forma que a classe Fantasma1.       
class Fantasma2 (Personagem):  
    
    def __init__(self,x,y,mx,my,s,f):
        super().__init__(x,y,mx,my,s)
        self.iPer = pygame.image.load('enemy2.png')        
        self.jogo=f   
        self.ponto=1
        self.direcao = "d"
        self.reposiciona()
    
    def movimenta(self): 
        if(self.direcao=="d"):
            self.movimentaXD()  
            if self.perX >= 736:
                self.direcao = "e"
                self.movimentaYB()
        if(self.direcao=="e"):
            self.movimentaXE()  
            if self.perX < 0:
                self.direcao = "d"
                self.movimentaYB()
                
    def reposiciona(self):
        self.perX = random.randint(0, 800)  
        self.perY = random.randint(50, 200) 
        
    def desenha(self):   
        b=self.jogo.getBala()  
       
        if(b!=None and b.getEstado()!="fim"): 
            colidiu=self.testaColisao(b) 
        else:
            colidiu=False
            
        if(colidiu==False):  
            self.movimenta()  
        else:  
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()  
            b.setEstado("fim")  
            self.jogo.addPlacar(self.ponto) 
            self.reposiciona()
        
        super().desenha()   
        
        
    def testaColisao(self,b):        
        distancia= math.sqrt(math.pow(self.perX - b.getX(), 2) + (math.pow(self.perY - b.getY(), 2)))
        if distancia < 27:
            return True
        else:
            return False


# A classe Bala é uma classe que define as balas disparadas pelo unicórnio. 
class Bala(Personagem):  
    
    def __init__(self,x,y,my,s):   
        super().__init__(x,y,0,my,s)
        self.iPer = pygame.image.load('bullet.png')
        self.perX = self.perX+16
        self.perY = self.perY-10
        self.somTiro = mixer.Sound("laser.wav")  
        self.somTiro.play()
        self.estado="fogo"
   
   
    def desenha(self):
        if self.perY <= 0:            
            self.estado = "fim"
        if self.estado=="fogo":   
            self.movimentaYC()            
            super().desenha()

    def getEstado(self):
        return self.estado
    
    def setEstado(self, e):
        self.estado=e
    
#A classe Fundo define o fundo do jogo. 
class Fundo: 

    def __init__(self,x,y,s):
        self.iFundo = pygame.image.load('background.png')
        self.fundoX = x
        self.fundoY = y
        self.scr=s
        
    def desenha(self):
        self.scr.blit(self.iFundo, (self.fundoX ,self.fundoY))

#A classe Texto é responsável por exibir o placar e mensagens na tela. 
class Texto:  
    
    def __init__(self,s):
        self.placar_fonte = pygame.font.Font('freesansbold.ttf', 32)
        self.fim_fonte = pygame.font.Font('freesansbold.ttf', 64)
        self.scr=s
    
    def mostra_placar(self,valor):  
        txt_placar = self.placar_fonte.render("Placar : " + str(valor), True, (255, 255, 255))
        self.scr.blit(txt_placar, (10, 10))

    def mostrar_fim_jogo(self): 
        txt_fim = self.fim_fonte.render("GAME OVER", True, (255, 105, 180))
        self.scr.blit(txt_fim, (200, 250))


#A classe Nivel é a classe principal do jogo e gerencia todos os personagens e objetos que aparecem na tela em um determinado nível. Por fim, a classe Jogo é a classe principal do jogo e é responsável por gerenciar todos os níveis e as transições entre eles.
class Nivel:
    
    def __init__(self,s,nFan,velocidade):
        self.scr=s
        self.numero_fantasmas = nFan
        self.velocidadeNivel=velocidade
        self.placar=0
             
        mixer.music.load("background.wav")
        mixer.music.play(-1)

        
        self.vOFantasmas1=[]    
        for i in range(self.numero_fantasmas):
            fan1=Fantasma1(0,0,4,40,self.scr,self)  
            self.vOFantasmas1.append(fan1) 
            
        self.oUnicornio=Unicornio(370,480,5,self.scr)  
        
        
        self.oBala=None   
        self.oFundo=Fundo(0,0,self.scr)
        self.oTexto=Texto(self.scr) 
        
        
        self.vOFantasmas2=[]    
        for r in range(self.numero_fantasmas):
            fan2=Fantasma2(0,0,4,40,self.scr,self)   
            self.vOFantasmas2.append(fan2)  
            
         
        self.oUnicornio=Unicornio(370,480,5,self.scr)  
         
        self.oBala=None  
        self.oFundo=Fundo(0,0,self.scr)  
        self.oTexto=Texto(self.scr)  
        

    def manipulaEvento(self,evento):                
        if evento.type == pygame.KEYDOWN:  
            if evento.key == pygame.K_LEFT:
                self.oUnicornio.movimentaXE()   
            if evento.key == pygame.K_RIGHT:
                self.oUnicornio.movimentaXD()      
            if evento.key == pygame.K_SPACE:  
                if(self.oBala==None or self.oBala.getEstado()=="fim"):  
                     self.oBala=Bala(self.oUnicornio.getX(),480,10,self.scr)


    def desenha(self):
        self.scr.fill((0, 0, 0))
        self.oFundo.desenha() 
     
        self.oUnicornio.desenha()  
        if(self.oBala!=None and self.oBala.getEstado()!="fim"):   
                    self.oBala.desenha()  
            
        fim=False
        for i in range(self.numero_fantasmas):  
                fan1t=self.vOFantasmas1[i]
                fan1t.desenha()   
                if(fan1t.getY()>450):  
                      fim=True
        fim=False
        for r in range(self.numero_fantasmas):  
                fan2t=self.vOFantasmas2[r]
                fan2t.desenha()   
                if(fan2t.getY()>450):  
                      fim=True           


        self.oTexto.mostra_placar(self.placar)  
            
        if (fim==True):
            self.oTexto.mostrar_fim_jogo()
                
        pygame.display.update()  

        return fim, self.placar  



    def addPlacar(self, pontos):
        self.placar+=pontos

    def getBala(self):
        return self.oBala


# A classe Jogo define o jogo e seu método __init__ inicializa as configurações iniciais do jogo,
#como a janela do jogo, o título e o ícone. Também define duas instâncias da classe Nivel, que representam
#os níveis do jogo. O método Jogar é responsável por executar o jogo, controlando o loop principal e
#manipulando os eventos do jogo. O loop principal é executado até que o jogo seja finalizado ou o jogador
#perca. Durante o loop principal, o método manipulaEvento da classe Nivel é chamado para manipular os eventos
#do jogo e atualizar o estado do jogo. O método desenha é chamado para desenhar os elementos do jogo na tela e,
#se o jogo for finalizado, o loop principal é encerrado. Se o jogador atingir uma pontuação suficiente, o próximo
#nível será iniciado. Quando o jogo é finalizado, a janela do jogo é fechada.

class Jogo:  

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  

        pygame.display.set_caption("Happy unicorn")
        icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(icon)

        self.niveis=[]
        n=Nivel(self.screen,3,30)  
        self.niveis.append(n)
        n=Nivel(self.screen,6,90)  
        self.niveis.append(n)

        self.nAtual=0

        self.Jogar()  


    def Jogar(self):
        clock = pygame.time.Clock()
        
        fimJogo=False
        running = True
        
        niv=self.niveis[self.nAtual]
        while running:   
            clock.tick(niv.velocidadeNivel)    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            if(fimJogo==False):
                niv.manipulaEvento(event)
                fimJogo, pontos = niv.desenha()   
                
                if(pontos>=15 and self.nAtual<1):
                    self.nAtual=self.nAtual+1
                    niv=self.niveis[self.nAtual]
            
        pygame.quit() 



    
if __name__=="__main__":
    j=Jogo()  
    