import pygame
import random
from constantes import *
from auxiliar import*
from plataforma import*
from balas import*


SPRITS_ENEMIGOS_R = {"imp": {"walk": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[0:3],
                             "idel": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[1:2],
                             "shoot": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[4:6],
                             "damege": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[6:8],
                             "arma": "plasma"},

                     "soldado 1": {"walk": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[0:4],
                                   "idel": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[1:2],
                                   "shoot": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[5:6],
                                   "damege": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[7:8],
                                   "arma": "escopeta"},

                     "soldado 2": {"walk": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[0:5],
                                   "idel": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[11:13],
                                   "shoot": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[6:7],
                                   "damege": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[8:10],
                                   "arma": "default"},

                     "super demonio": {"walk": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[0:3],
                                       "idel": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[9:11],
                                       "shoot": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[4:5],
                                       "damege": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[6:8],
                                       "arma": "energia"},
                     }

SPRITS_ENEMIGOS_L = {"imp": {"walk": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[0:3],
                             "idel": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3)[1:2],
                             "shoot": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[4:6],
                             "damege": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[6:8]},

                     "soldado 1": {"walk": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[0:3],
                                   "idel": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[1:2],
                                   "shoot": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[5:6],
                                   "damege": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3)[7:8]},

                     "soldado 2": {"walk": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4,)[0:5],
                                   "idel": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4,)[11:13],
                                   "shoot": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4,)[6:7],
                                   "damege": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4,)[8:10]},

                     "super demonio": {"walk": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3,)[0:3],
                                       "idel": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3,)[9:11],
                                       "shoot": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3,)[4:5],
                                       "damege": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3,)[6:8]}
                     }

class Enemigo(pygame.sprite.Sprite):

    def __init__(self,x,y,velocidad,framerate_animacion,framerate_moviemiento,tipo_enemigo) -> None:

        pygame.sprite.Sprite.__init__(self)
        self.direccion = DIRECCION_R
        self.tipo_enemigo = tipo_enemigo
        self.arma = SPRITS_ENEMIGOS_R[tipo_enemigo]["arma"]
        self.salud = 50
        self.salud_maxima = self.salud
        self.vivo = True
        self.contador_caida = 0
        self.speed = velocidad
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.cooldown_dispario = 0
        self.cooldown_maximo = 15
        self.animacion = SPRITS_ENEMIGOS_R[tipo_enemigo]["idel"]
        self.image = self.animacion[self.frame]
        self.mask = self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_trasncurrio_moviento = 0
        self.tiempo_trasncurrio_animacion = 0
        self.frame_rate_animacion = framerate_animacion
        self.frame_rate_movimiento = framerate_moviemiento
        self.disparando = False
        self.grupo_balas = pygame.sprite.Group()

        self.contador_movimieno = 0
        self.rect_vision = pygame.Rect(0,0,300,100)
        self.rect_vision.center = (self.rect.centerx + 75, self.rect.centery)


    def caminar_ia(self,player,):

        if self.vivo and player.vivo:

            if self.direccion == DIRECCION_R:

                self.animacion = SPRITS_ENEMIGOS_R[self.tipo_enemigo]["walk"]
                self.mover_x = self.speed

            else:

                self.animacion = SPRITS_ENEMIGOS_L[self.tipo_enemigo]["walk"]
                self.mover_x = -self.speed



            # self.rect_vision.center = (self.rect.centerx + 75 * direccion,self.rect.centery)


            if self.frame > len(self.animacion)-1:
                self.frame = 0


            pass

    def disparar(self):

        if self.direccion == DIRECCION_R:

            self.animacion = SPRITS_ENEMIGOS_R[self.tipo_enemigo]["shoot"]

        else:

            self.animacion = SPRITS_ENEMIGOS_L[self.tipo_enemigo]["shoot"]

        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0

    def quieto(self):

        # if self.animacion != SPRITS_JUGADOR_R[self.arma]["idel"] and self.animacion != SPRITS_JUGADOR_L[self.arma]["idel"]:

            if self.direccion == DIRECCION_R:

                self.image = SPRITS_ENEMIGOS_R[self.tipo_enemigo]["idel"]

            else:

                self.image = SPRITS_ENEMIGOS_L[self.tipo_enemigo]["idel"]



            self.mover_x = 0
            self.mover_y = 0
            self.frame = 0

    def landed(self):

        self.mover_y = 0
        self.contador_caida = 0
        self.contador_salto = 0

    def hit_head(self):

        self.mover_y *= -1

    def colicion_vertical(self,objetos:list[Objeto],desplazamineto_y):


        for obj in objetos:

            if obj.rect.colliderect(self.rect.x,self.rect.y + self.mover_y,self.ancho,self.alto):

                    if desplazamineto_y >= 0:

                        self.rect.bottom = obj.rect.top
                        self.landed()

                    elif desplazamineto_y < 0:

                        self.rect.top = obj.rect.bottom
                        self.hit_head()

    def colicion_horizontal(self,objetos):

        for obj in objetos:

            if obj.rect.colliderect(self.rect.x + self.mover_x,self.rect.y -0.1,self.ancho,self.alto):

                    if self.rect.x >= obj.rect.x +6:

                        self.quieto()
                    elif self.rect.x  >= -obj.rect.x + 6:

                        self.quieto()

    def vision(self,player):

        if self.rect_vision.colliderect(player.rect.x,player.rect.y,player.ancho,player.alto):

            self.disparar()
            self.disparando = True

        else:

            self.disparando =  False

    def daño(self,cantidad_daño):

        self.salud = - cantidad_daño

        if self.salud == 0:

            self.kill()

    def ia(self,objetos,player):

        lista_distancia = [TAM_BLOQUE*2,TAM_BLOQUE**2,TAM_BLOQUE*3,]

        distancia = random.choice(lista_distancia)

        self.caminar_ia(player)

        self.contador_movimieno += 1

        if self.contador_movimieno > distancia:

            distancia = random.choice(lista_distancia)

            if self.direccion == DIRECCION_L:
                self.rect_vision.center = (self.rect.centerx + 75, self.rect.centery)
                self.direccion = DIRECCION_R
            else:
                self.rect_vision.center = (self.rect.centerx + 75 * -1, self.rect.centery)
                self.direccion = DIRECCION_L

            self.contador_movimieno = 0

        self.colicion_horizontal(objetos)
        self.colicion_vertical(objetos,self.mover_y)

    def balas(self,screen):

        self.grupo_balas.draw(screen)

        self.grupo_balas.update(self)

    def do_moviento(self,delta_ms,player,objetos):

        self.mover_y += min(1, (self.contador_caida / FPS) * GRAVEDAD)

        self.tiempo_trasncurrio_moviento += delta_ms

        if self.tiempo_trasncurrio_moviento >= self.frame_rate_movimiento:

            self.update_bala()

            self.ia(objetos,player)

            self.vision(player)

            self.add_x(self.mover_x)
            self.add_y(self.mover_y)

            self.tiempo_trasncurrio_moviento = 0

        self.contador_caida += 1

    def update_bala(self):

        if self.disparando and self.cooldown_dispario == 0:

            if self.direccion == 0:

                self.grupo_balas.add(Bala(self.rect.centerx + self.rect.size[0]/2,self.rect.centery,self.direccion,self.arma))

            else:


                self.grupo_balas.add(Bala(self.rect.centerx - self.rect.size[0]/2,self.rect.centery,self.direccion,self.arma))


            self.cooldown_dispario = self.cooldown_maximo


        elif self.cooldown_dispario > 0:

            self.cooldown_dispario -= 1


        pass

    def ia_movimientos(self,objetos):

        if self.direccion == DIRECCION_R and self.mover_x > self.ancho*2:

            self.mover_x = self.speed


        elif self.mover_x < TAM_BLOQUE  and self.mover_x < self.ancho*2:

            self.mover_x = -self.speed

        self.colicion_horizontal(objetos)
        self.colicion_vertical(objetos,self.mover_y)

    def add_x(self,delta_x):

        self.rect.x += delta_x
        self.rect_vision.x += delta_x
        pass

    def add_y(self,delta_y):

        self.rect.y += delta_y
        self.rect_vision.y = self.rect.y

    def do_animacion(self,delta_ms):
        self.tiempo_trasncurrio_animacion += delta_ms

        if self.mover_y > 0:

            self.on_air = True

        if self.tiempo_trasncurrio_animacion >= self.frame_rate_animacion:

            self.tiempo_trasncurrio_animacion = 0

            if self.frame < (len(self.animacion) -1):


                self.frame += 1

            else:

                self.frame = 0


        if self.cooldown_dispario > 0:
            self.cooldown_dispario -= 1

    def update(self,delta_ms,player,objetos):
        self.do_moviento(delta_ms,player,objetos)
        self.do_animacion(delta_ms)

    def draw(self,screen):


        if DEBUG:

            pygame.draw.rect(screen,ROJO,self.rect)
            pygame.draw.rect(screen,VERDE,self.rect_vision)


        self.balas(screen)
        self.image = self.animacion[self.frame]
        screen.blit(self.image,self.rect)

