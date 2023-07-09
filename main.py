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

items = Items(200,400,"escudo")

items_group.add(items)

nivel = Nivel(NIVELES[0]["prueba"],columnas_nivel=15,filas_nivel=26)

nivel.prosesar_data()


# bloque_1 = Plataforma(x= 100,y= 300,tamaño=TAM_BLOQUE,path=(r"{}{}".format(PHAT_RECURSOS,PAHT_BLOQUES_AZUL)),columna_x= 1,fila_y= 0)

player = Jugador(x=10, y=10, velocidad=6,framerate_animacion= 150 , framerate_moviemiento= 18)





# for i  in range(-ANCHO_VENTANA // TAM_BLOQUE ,ANCHO_VENTANA*2// TAM_BLOQUE):

#     bloque = Plataforma(x= i * TAM_BLOQUE,y=500,tamaño=TAM_BLOQUE,path=r"C:\Users\pablo\OneDrive\Escritorio\pygame 2023\mis imagenes\locations\bloques\bloques.png",columna_x= 0,fila_y= 0)
    
#     piso.append(bloque)


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
            
        player.control_vertical(nivel.lista_ostaculos,evento)


    
    if flag_pausa:

        flag_pausa,corriendo = pausa.draw(screen)

        print(flag_pausa)

    else:

        delta_ms = clock.tick(FPS)
        player.control_horizontal(nivel.lista_ostaculos)
        player.update(delta_ms)
        player.draw(screen)
        items_group.update(player)
        items_group.draw(screen)
        nivel.draw(screen)
    
    pygame.display.flip()
    screen.blit(fondo,fondo.get_rect())
                            
