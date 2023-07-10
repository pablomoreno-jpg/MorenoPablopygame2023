import pygame
import sys
from constantes import *
from jugador import*
from auxiliar import*
from plataforma import*
from niveles import*
from items import*
from barras import*
from menus_gui import*


screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()
clock = pygame.time.Clock()


pygame.display.set_caption("doom's gate")

fondo = pygame.image.load(r"{0}\locations\forest\all.png".format(PHAT_RECURSOS))
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))


items_group = pygame.sprite.Group()

items = Items(200,400,"plasma")

items_group.add(items)

nivel = Nivel(NIVELES[0]["prueba"],columnas_nivel=33,filas_nivel=22)

nivel.prosesar_data()

player = Jugador(x=40, y=10, velocidad=6,framerate_animacion= 200, framerate_moviemiento= 18)
enemigo = Enemigo(x=100, y =60,velocidad=4,framerate_animacion= 200, framerate_moviemiento= 18,tipo_enemigo="soldado 2")


flag_pausa = False
corriendo = True

pausa = Pausa(corriendo)

while corriendo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                
                flag_pausa = True
            
        player.control_vertical(nivel.lista_solidos,evento,nivel.lista_trampas)


    
    if flag_pausa:

        flag_pausa,corriendo = pausa.draw(screen)


    else:

        delta_ms = clock.tick(FPS)
        nivel.draw(screen)
        player.control_horizontal(nivel.lista_solidos,nivel.lista_trampas)
        player.update(delta_ms)
        player.draw(screen)
        # enemigo.draw(screen)
        # enemigo.ia_movimientos(nivel.lista_solidos)
        # enemigo.update(delta_ms)
        items_group.update(player)
        items_group.draw(screen)
        

    pygame.display.flip()
    screen.blit(fondo,fondo.get_rect())
                            
