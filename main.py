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

# fuente = pygame.font.Font(PAHT_FONT,50)
# texto = fuente.render("no  hay juego",0,VERDE)

#set_cronometro:d

evento_1000s = pygame.USEREVENT
pygame.time.set_timer(evento_1000s,1000)
segudos = 59
minutos = 5

pygame.display.set_caption("doom's gate")

#fondos auxiliar
fondo = Auxliar.elegir_background("prueba")

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
sengudos_transcurridos =  0
crear_enemigo = True
crear_item = True



while corriendo:

    delta_ms = clock.tick(FPS)

   

    if flag_comenzar_juego == False:
        
        segudos = 59
        minutos = 5

        flag_eligiendo_nivel, corriendo = menu_principal.draw(screen)

        if flag_eligiendo_nivel:

            flag_nivel_cargado = elegir_niveles.draw(screen)

        if flag_nivel_cargado:

            fondo = Auxliar.elegir_background(elegir_niveles.nombre_nivel)
            nivel = Nivel(NIVELES[elegir_niveles.nombre_nivel], columnas_nivel=33, filas_nivel=22)
            player = nivel.prosesar_data()

            flag_comenzar_juego = True
    else:
        
        if flag_pausa:

            flag_pausa,corriendo = pausa.draw(screen)

        else:
            
            tiempo = Auxliar.generar_texto(PAHT_FONT,50,"{0}:{1}".format(minutos,segudos),BLANCO)

            nivel.draw(screen)
            player.update(delta_ms)
            player.draw(screen)
            player.control_horizontal(nivel.lista_solidos,nivel.lista_trampas)

            for item in nivel.item_group:

                item.update(player)
                item.draw(screen)

            for enemigo in nivel.enemy_group:

                enemigo.update(delta_ms,player,nivel.lista_solidos)
                enemigo.draw(screen)

            
                colicion_bala_personajas(player,enemigo)
            
            imprimir_texto(screen,tiempo,ANCHO_VENTANA/2,50,tamaño_mensaje_x= 50)
            
            if sengudos_transcurridos == 10:
    
                if crear_item:
                    nivel.volver_a_cargar_items()
                    crear_item = False

            if sengudos_transcurridos == 15:
                
                sengudos_transcurridos = 0
                if crear_enemigo:
                    nivel.volver_a_cargar_enemigo()
                    crear_enemigo = False

            if sengudos_transcurridos == 0:

                crear_item = True
                crear_enemigo = True

            flag_comenzar_juego = terminador_partida(player,segudos,minutos,screen)
            flag_nivel_cargado = flag_comenzar_juego
            flag_eligiendo_nivel = flag_comenzar_juego

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

        if evento.type == evento_1000s and flag_pausa == False:
            if segudos > 0:
                segudos -= 1
                
            else:
                minutos -= 1
                segudos = 60

            if flag_comenzar_juego and flag_pausa == False:
                sengudos_transcurridos += 1

        
    # pygame.display.flip()
    # screen.blit(fondo,fondo.get_rect())