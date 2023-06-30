import pygame
import sys
from constantes import *
from jugador import*
from auxiliar import*
from plataforma import*
from niveles import*

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()
clock = pygame.time.Clock()

fondo = pygame.image.load(r"{0}\locations\forest\all.png".format(PHAT_RECURSOS))
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

bloque_1 = Plataforma(x= 100,y= 300,tamaño=TAM_BLOQUE,path=(r"{}{}".format(PHAT_RECURSOS,PAHT_BLOQUES_AZUL)),columna_x= 1,fila_y= 0)

player = Jugador(x=10, y=10, velocidad=6,framerate_animacion= 150 , framerate_moviemiento= 18)

piso = []

for i  in range(-ANCHO_VENTANA // TAM_BLOQUE ,ANCHO_VENTANA*2// TAM_BLOQUE):

    bloque = Plataforma(x= i * TAM_BLOQUE,y=500,tamaño=TAM_BLOQUE,path=(r"{}{}".format(PHAT_RECURSOS,PAHT_BLOQUES_AZUL)),columna_x= 0,fila_y= 0)
    
    piso.append(bloque)


while True:


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

        
            
        player.control_vertical(piso,evento)




    delta_ms = clock.tick(FPS)
    player.control_horizontal(piso)
    # bloque.draw(screen)
    dibujar_piso(screen,piso)
    player.update(delta_ms)
    player.draw(screen)
  

    
    pygame.display.flip()
    screen.blit(fondo,fondo.get_rect())
                            
