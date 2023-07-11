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


# fuente = pygame.font.Font(PAHT_FONT,100)
# texto = fuente.render("hola",0,ROJO)


pygame.display.set_caption("doom's gate")

fondo = pygame.image.load(r"{0}\locations\forest\all.png".format(PHAT_RECURSOS))
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

enemy_grupe = pygame.sprite.Group()
items_group = pygame.sprite.Group()

items = Items(200,400,"plasma")

items_group.add(items)

nivel = Nivel(NIVEL_02,columnas_nivel=33,filas_nivel=22)

player = nivel.prosesar_data()

# player = Jugador(x=40, y=10, velocidad=6,framerate_animacion= 200, framerate_moviemiento= 18)
# enemigo1 = Enemigo(x=500, y =60,velocidad=4,framerate_animacion= 200, framerate_moviemiento= 18,tipo_enemigo="soldado 1")
# enemigo = Enemigo(x=500, y =60,velocidad=4,framerate_animacion= 200, framerate_moviemiento= 18,tipo_enemigo="super demonio")

# enemy_grupe.add(enemigo)
# enemy_grupe.add(enemigo1)

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


        for item in nivel.item_group:

            item.update(player)
            item.draw(screen)
        
    # screen.blit(texto,(ANCHO_VENTANA/2 - 200,100))
    pygame.display.flip()
    screen.blit(fondo,fondo.get_rect())
                            
