import pygame
from constantes import *
from auxiliar import*
from plataforma import*
from balas import*


SPRITS_ENEMIGOS_R = {"imp": {"walk": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[0:2],
                             "idel": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[1:2],
                             "shoot": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[3:5],
                             "damege": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[6:8]},

                     "soldado 1": {"walk": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[0:4],
                                   "idel": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[1:2],
                                   "shoot": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[5:6],
                                   "damege": Auxliar.load_sprisheet(r"{}\soldado 1.png".format(PAHT_ENEMIGOS), columnas=3, filas=3, direcciones=True)[7:8]},

                     "soldado 2": {"walk": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[0:5],
                                   "idel": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[11:13],
                                   "shoot": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[6:7],
                                   "damege": Auxliar.load_sprisheet(r"{}\soldado 2.png".format(PAHT_ENEMIGOS), columnas=4, filas=4, direcciones=True)[8:10]},

                     "super demonio": {"walk": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[0:3],
                                       "idel": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[9:11],
                                       "shoot": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[4:5],
                                       "damege": Auxliar.load_sprisheet(r"{}\super demonio.png".format(PAHT_ENEMIGOS), columnas=4, filas=3, direcciones=True)[6:8]}
                     }

SPRITS_ENEMIGOS_L = {"imp": {"walk": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[0:2],
                             "idel": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3)[1:2],
                             "shoot": Auxliar.load_sprisheet(r"{}\imp.png".format(PAHT_ENEMIGOS), columnas=3, filas=3,)[3:5],
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
        
        super().__init__()
        self.direccion = DIRECCION_R
        self.tipo_enemigo = tipo_enemigo
        self.salud = 50
        self.salud_maxima = self.salud
        self.vivo = True
        self.contador_salto = 0
        self.contador_caida = 0
        self.speed = velocidad
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.cooldown_dispario = 0
        self.cooldown_maximo = 15
        self.animacion = SPRITS_ENEMIGOS_R[tipo_enemigo]["idel"]
        self.imagen = self.animacion[self.frame]
        self.mask = self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect()
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_trasncurrio_moviento = 0
        self.tiempo_trasncurrio_animacion = 0
        self.frame_rate_animacion = framerate_animacion
        self.frame_rate_movimiento = framerate_moviemiento
        self.disparando = False
        self.salto = False
        self.grupo_balas = pygame.sprite.Group()
        
        self.contador_movimieno = 0


    def caminar_ia(self,direccion):

        # if self.direccion != direccion or (self.animacion != self.caminar_r or self.animacion != self.caminar_l):

        if self.vivo:

            self.direccion = direccion
        

            if direccion == DIRECCION_R:

                    self.mover_x = self.speed

                    self.animacion = SPRITS_ENEMIGOS_R[self.tipo_enemigo]["walk"]
                    
            else:
                    self.mover_x = -self.speed

                    self.animacion = SPRITS_ENEMIGOS_L[self.tipo_enemigo]["walk"]
            
            self.contador_movimieno += 1


            if self.contador_movimieno > TAM_BLOQUE:

                self.mover_x *= -1


            if self.frame > len(self.animacion) -1:

                self.frame = 0
   
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
                
                self.imagen = SPRITS_ENEMIGOS_R[self.tipo_enemigo]["idel"]

            else:
                
                self.imagen = SPRITS_ENEMIGOS_L[self.tipo_enemigo]["idel"]

            

            self.mover_x = 0
            self.mover_y = 0
            self.frame = 0

    def landed(self):
        
        self.mover_y = 0
        self.contador_caida = 0
        self.contador_salto = 0

    def hit_head(self):

        self.mover_y *= -1

    def colicion_horizontal(self,objetos:list[Objeto]):

        coleccion_objetos = []

        for obj in objetos:

            if pygame.sprite.collide_mask(self,obj):
                    
                if self.mover_y >= 0:

                    self.rect.bottom = obj.rect.top
                    self.landed()


            
        return coleccion_objetos

    def collide(self,objetos,):
        pass
    
    def balas(self,screen):

        self.grupo_balas.draw(screen)

        self.grupo_balas.update(self)

    def do_moviento(self,delta_ms):


        self.mover_y += min(1, (self.contador_caida / FPS) * GRAVEDAD)


        self.tiempo_trasncurrio_moviento += delta_ms

        if self.tiempo_trasncurrio_moviento >= self.frame_rate_movimiento:

            self.update_bala()

            if self.mover_y > 0:

                self.salto = False


            self.add_x(self.mover_x)
            self.add_y(self.mover_y)


            self.tiempo_trasncurrio_moviento = 0

        self.contador_caida += 1

    def update_bala(self):

        if self.disparando and self.frame == 1 and self.cooldown_dispario == 0:
    
            if self.direccion == DIRECCION_R:
                

                self.grupo_balas.add(Bala(self.rect.centerx + self.rect.size[0],self.rect.centery,self.direccion,self.arma))
            
            else:
                
                self.grupo_balas.add(Bala(self.rect.centerx - self.rect.size[0],self.rect.centery,self.direccion,self.arma))

            
            self.cooldown_dispario = self.cooldown_maximo

    
        elif self.cooldown_dispario > 0:

            self.cooldown_dispario -= 1

        pass

    def add_x(self,delta_x):

        self.rect.x += delta_x

        pass
    
    def add_y(self,delta_y):

        self.rect.y += delta_y

        pass

    def update_mask(self):

        self.rect = self.imagen.get_rect(topleft = (self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.imagen)

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

    def update(self,delta_ms):

        self.do_moviento(delta_ms)
        self.do_animacion(delta_ms)
        self.update_mask()  
        
    def draw(self,screen):

        # self.salud_escudo.draw(self.salud,self.escudo,screen)
        
        if DEBUG:

            pygame.draw.rect(screen,ROJO,self.rect)
            # pygame.draw.rect(screen,VERDE,self.side_collide_r)

        self.balas(screen)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)

