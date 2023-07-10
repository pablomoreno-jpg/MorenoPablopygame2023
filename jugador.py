import pygame
from constantes import*
from auxiliar import*
from plataforma import*
from balas import*
from barras import*

SPRITS_JUGADOR_L = {"default":{"idel":Auxliar.load_sprisheet(r"{0}\characters\doom marine\default\idel.png".format(PHAT_RECURSOS),2,1),
                              "shoot": Auxliar.load_sprisheet(r"{0}\characters\doom marine\default\shoot.png".format(PHAT_RECURSOS),3,1),
                              "walk":Auxliar.load_sprisheet(r"{0}\characters\doom marine\default\walk.png".format(PHAT_RECURSOS),4,1)},
                "escopeta":{"idel":Auxliar.load_sprisheet(r"{0}\characters\doom marine\escopeta\idel.png".format(PHAT_RECURSOS),8,1),
                              "shoot": Auxliar.load_sprisheet(r"{0}\characters\doom marine\escopeta\shoot.png".format(PHAT_RECURSOS),5,1),
                              "walk":Auxliar.load_sprisheet(r"{0}\characters\doom marine\escopeta\walk.png".format(PHAT_RECURSOS),3,1)},
                "salto":Auxliar.load_sprisheet(r"{0}\characters\doom marine\jump.png".format(PHAT_RECURSOS),5,1)}

SPRITS_JUGADOR_R = {"default":{"idel":Auxliar.load_sprisheet(r"{0}\characters\doom marine\default\idel.png".format(PHAT_RECURSOS),2,1,direcciones=True),
                              "shoot": Auxliar.load_sprisheet(r"{0}\characters\doom marine\default\shoot.png".format(PHAT_RECURSOS),3,1,direcciones=True),
                              "walk":Auxliar.load_sprisheet(r"{0}\characters\doom marine\default\walk.png".format(PHAT_RECURSOS),4,1,direcciones=True)},
                "escopeta":{"idel":Auxliar.load_sprisheet(r"{0}\characters\doom marine\escopeta\idel.png".format(PHAT_RECURSOS),8,1,direcciones=True),
                              "shoot": Auxliar.load_sprisheet(r"{0}\characters\doom marine\escopeta\shoot.png".format(PHAT_RECURSOS),5,1,direcciones=True),
                              "walk":Auxliar.load_sprisheet(r"{0}\characters\doom marine\escopeta\walk.png".format(PHAT_RECURSOS),3,1,direcciones=True)},
                "salto":Auxliar.load_sprisheet(r"{0}\characters\doom marine\jump.png".format(PHAT_RECURSOS),5,1,direcciones=True)}

class Jugador(pygame.sprite.Sprite):

    def __init__(self,x,y,velocidad,framerate_animacion,framerate_moviemiento) -> None:
        super().__init__()
        self.direccion = DIRECCION_R
        self.arma = "default"
        self.salud = 100
        self.salud_maxima = self.salud
        self.escudo_maximo = 50
        self.escudo = 0
        self.grandas_maximas = 6
        self.grandas = 0
        self.misiles_maximos = 10
        self.munision_misiles = 0
        self.contador_salto = 0
        self.contador_caida = 0
        self.speed = velocidad
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.cooldown_dispario = 0
        self.cooldown_maximo = 15
        self.animacion = SPRITS_JUGADOR_R[self.arma]["idel"]
        self.imagen = self.animacion[self.frame]
        self.mask = self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect()
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()
        self.rect.x = x
        self.rect.y = y
        self.posicion_inicial = y
        self.tiempo_trasncurrio_moviento = 0
        self.tiempo_trasncurrio_animacion = 0
        self.frame_rate_animacion = framerate_animacion
        self.frame_rate_movimiento = framerate_moviemiento
        self.disparando = False
        self.salto = False
        # self.aterrisaje = False
        self.grupo_balas = pygame.sprite.Group()
        self.salud_escudo = BarraSalud(x=10,y=40,barra_salud=self.salud,salud_maxima=self.salud_maxima,escudo=self.escudo,escudo_maximo=self.escudo_maximo)
        
    def caminar(self,direccion):

        # if self.direccion != direccion or (self.animacion != self.caminar_r or self.animacion != self.caminar_l):
            
            self.direccion = direccion

            if direccion == DIRECCION_R:

                    self.mover_x = self.speed

                    self.animacion = SPRITS_JUGADOR_R[self.arma]["walk"]
                    
            else:

                    self.mover_x = -self.speed

                    self.animacion = SPRITS_JUGADOR_L[self.arma]["walk"]
            
            if self.frame > len(self.animacion) -1:

                self.frame = 0

    def saltar(self):

        self.salto = True
        self.mover_y = -GRAVEDAD * 10
        self.frame = 0
        self.contador_salto += 1
        if self.contador_salto == 1:
            self.contador_caida = 0

        if self.contador_salto == 2:

            self.mover_y -=  4

        if self.direccion == DIRECCION_R:
    
            self.animacion = SPRITS_JUGADOR_R["salto"]

        else:

            self.animacion = SPRITS_JUGADOR_L["salto"]

    def disparar(self):

        if self.direccion == DIRECCION_R:

            self.animacion = SPRITS_JUGADOR_R[self.arma]["shoot"]
        else:

            self.animacion = SPRITS_JUGADOR_L[self.arma]["shoot"]


        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0

    def quieto(self):

        if self.animacion != SPRITS_JUGADOR_R[self.arma]["idel"] and self.animacion != SPRITS_JUGADOR_L[self.arma]["idel"]:

            if self.direccion == DIRECCION_R:

                self.animacion = SPRITS_JUGADOR_R[self.arma]["idel"]

            else:
                
                self.animacion = SPRITS_JUGADOR_L[self.arma]["idel"]

            self.mover_x = 0
            self.mover_y = 0

            if self.frame > len(self.animacion) -1:
                
                self.frame = 0

    def landed(self,rect):
        
        self.mover_y = rect - self.rect.bottom
        self.contador_caida = 0
        self.contador_salto = 0

    def hit_head(self):

        self.mover_y *= -1

    def colicion_vertical(self,objetos:list[Objeto],desplazamineto_y):

        coleccion_objetos = []

        for obj in objetos:

            if pygame.sprite.collide_mask(self,obj):
                
                if not self.salto:
                    
                    if desplazamineto_y >= 0:

                        self.rect.bottom = obj.rect.top
                        self.landed(obj.rect.top)
                        # self.aterrisaje = True

                

            # if obj.rect.colliderect(self.rect.x + self.mover_x,self.rect.y -0.1,self.ancho,self.alto):

            #         if self.rect.x >= obj.rect.x +6:

            #             self.mover_x = 0

            #         elif (self.rect.x - 10)  >  - (obj.rect.x + 10):
            #             print("va a tocar")
                    
            #             self.mover_x = 0
                    


            # else:

            #     self.aterrisaje = False


        return coleccion_objetos

    def colicion_horizontal(self,objetos,):

        for obj in objetos:


            if obj.rect.colliderect(self.rect.x + self.mover_x,self.rect.y -0.1,self.ancho,self.alto):

                    if self.rect.x >= obj.rect.x +6:

                        self.mover_x = 0

                    elif (self.rect.x + 30) >= -obj.rect.x and self.rect.bottom != obj.rect.top:
                        
                        print("va a tocar")
                        self.quieto()


    def control_horizontal(self,objeto):

        keys = pygame.key.get_pressed()

        # collide_izquierda = self.collide(objeto,-1)
        # collide_derecha = self.collide(objeto,1)


        if not keys[pygame.K_SPACE] and not keys[pygame.K_l] :

            if (keys[pygame.K_d] and not keys[pygame.K_a]) :

                self.caminar(DIRECCION_R)

            if (keys[pygame.K_a] and not keys[pygame.K_d]) :

                self.caminar(DIRECCION_L)

            if not keys[pygame.K_a] and not keys[pygame.K_d]:

                self.quieto()

            if  keys[pygame.K_a] and  keys[pygame.K_d]:

                self.quieto()
            
            self.colicion_horizontal(objeto)

        self.colicion_vertical(objeto,self.mover_y)
        
    def control_vertical(self,objeto:list[Objeto],evento):

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE and self.contador_salto < 2:
                        
                self.saltar()
            
            if evento.key == pygame.K_l:
                self.disparando = True
                self.disparar()

        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_l:

                self.disparando = False
        
        self.colicion_vertical(objeto,self.mover_y)
    
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
        self.salud_escudo.draw(self.salud,self.escudo,screen)
        if DEBUG:

            pygame.draw.rect(screen,ROJO,self.rect)
            # pygame.draw.rect(screen,VERDE,self.side_collide_r)

        self.balas(screen)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)

