# Jogo-Pygame
Jogo simples com níveis e pontuação

Jogo em Python usando a biblioteca Pygame. A classe Personagem é a classe pai, que contém funções para movimentar e desenhar personagens, além de funções para obter as coordenadas x e y de um personagem.
A classe Unicornio herda da classe Personagem e é usada para criar o personagem principal do jogo, que pode mover-se para a direita e esquerda dentro da janela do jogo.
A classe Fantasma1 também herda da classe Personagem e é usada para criar um personagem inimigo que se move horizontalmente de um lado para o outro na janela do jogo. 
A classe Fantasma2 é usada para criar um segundo tipo de personagem inimigo que funciona da mesma forma que a classe Fantasma1.
As classes contêm funções para testar a colisão entre os personagens inimigos e as balas do jogador, aumentando a pontuação do jogador e reposicionando os personagens inimigos em novas posições aleatórias quando uma colisão é detectada.
