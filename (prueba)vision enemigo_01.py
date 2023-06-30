import pygame

#ventana
ANCHO_VEN = 400
ALTO_VEN = 500

#jugadaor rectangulo
ALTO = 20
ANCHO = 30
VELOCIDAD = 6
POS_X = int(ANCHO_VEN * 0.8)
POS_Y = 100

#enemigo VISION:
LARGO = 70
CARRERA = 2
POS_X_EN = int(ANCHO_VEN * 0.2)
POS_Y_EN = 100

flag_seguir = True

pygame.init()
pantalla = pygame.display.set_mode((ALTO_VEN,ANCHO_VEN))
reloj = pygame.time.Clock()
corriendo = True



while corriendo:

    tiempo = pygame.time.get_ticks() // 100

    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:

            corriendo = False

    #jugador

    if POS_Y < 300  :

        POS_Y += 10

    botonos = pygame.key.get_pressed()

    if botonos[pygame.K_d]:
            
        POS_X += VELOCIDAD
    
    if botonos [pygame.K_a]:

        POS_X -= VELOCIDAD

    if botonos [pygame.K_w]:

        POS_Y -= VELOCIDAD

    if botonos [pygame.K_s]:

        POS_Y += VELOCIDAD

    pantalla.fill((255,255,250))

    #enemigo:
    # vision_enemiga = pygame.draw.circle(pantalla,(0,0,255),(POS_X_EN+(ANCHO//2),POS_Y_EN+(ALTO//2)),100)
    # colicion_enemiga = pygame.draw.rect(pantalla,(255,0,0),(POS_X_EN,POS_Y_EN,ANCHO,ALTO))
    #jugador:
    jugador = pygame.draw.rect(pantalla,(0,255,0),(POS_X,POS_Y,ANCHO,ALTO))


    jugador.bo
    # if vision_enemiga.colliderect(jugador):
        
    #     if flag_seguir:
            
    #         mover_x = jugador.x
    #         mover_y = jugador.y
    #         flag_seguir = False
        
    # if not flag_seguir:

    #     if POS_X_EN < mover_x:

    #         POS_X_EN += CARRERA

    #     elif POS_X_EN > mover_x:

    #         POS_X_EN -= CARRERA

    #     if POS_Y_EN < mover_y:

    #         POS_Y_EN += CARRERA

    #     elif POS_Y_EN > mover_y:

    #         POS_Y_EN -= CARRERA

    #     if POS_X_EN == mover_x and POS_Y_EN == mover_y:

    #         flag_seguir = True

    # if colicion_enemiga.colliderect(jugador):

    #     print("PUM!")

    


    pygame.display.flip()

    reloj.tick(60)

pygame.quit()


