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


fuente = pygame.font.Font(PAHT_FONT,50)
texto = fuente.render("no  hay juego",0,ROJO)


pygame.display.set_caption("doom's gate")

# fondo = pygame.image.load(r"{0}\locations\forest\all.png".format(PHAT_RECURSOS))
# fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

#fondos
fondo = Auxliar.elegir_background("prueba")

enemy_grupe = pygame.sprite.Group()
items_group = pygame.sprite.Group()

items = Items(200,400,"plasma")

items_group.add(items)

# nivel = Nivel(NIVELES["nivel 2"],columnas_nivel=33,filas_nivel=22)

# player = nivel.prosesar_data()

flag_nivel_cargado = False
flag_pausa = False
flag_eligiendo_nivel = False
flag_comenzar_juego = False
corriendo = True


pausa = Pausa(corriendo)
menu_principal = Main_menu(corriendo)
elegir_niveles = Niveles()
nivel = Nivel(NIVELES[elegir_niveles.nombre_nivel], columnas_nivel=33, filas_nivel=22)
player = nivel.prosesar_data()

while corriendo:

    delta_ms = clock.tick(FPS)

   

    if flag_comenzar_juego == False:
        
        flag_eligiendo_nivel, corriendo = menu_principal.draw(screen)


        if flag_eligiendo_nivel:

            flag_nivel_cargado = elegir_niveles.draw(screen)

        
        if flag_nivel_cargado:

            fondo = Auxliar.elegir_background(elegir_niveles.nombre_nivel)
            nivel = Nivel(NIVELES[elegir_niveles.nombre_nivel], columnas_nivel=33, filas_nivel=22)
            player = nivel.prosesar_data()

            flag_comenzar_juego = True
            print(type(player))
    else:

        if flag_pausa:

            flag_pausa,corriendo = pausa.draw(screen)

        else:

            nivel.draw(screen)
            player.control_horizontal(nivel.lista_solidos,nivel.lista_trampas)
            player.update(delta_ms)
            player.draw(screen)


            for item in nivel.item_group:

                item.update(player)
                item.draw(screen)
            
        # screen.blit(texto,(ANCHO_VENTANA/2 - 200,100))
        # pygame.display.flip()
        # screen.blit(fondo,fondo.get_rect())
    
    pygame.display.flip()
    screen.blit(fondo,fondo.get_rect())                      
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                
                flag_pausa = True
            
        if flag_nivel_cargado == True:
            player.control_vertical(nivel.lista_solidos,evento,nivel.lista_trampas)
    
    # pygame.display.flip()
    # screen.blit(fondo,fondo.get_rect())