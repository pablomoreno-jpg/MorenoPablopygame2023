import pygame
from constantes import*
from auxiliar import*
from plataforma import*
from balas import*

class Jugador(pygame.sprite.Sprite):

    def __init__(self,x,y,velocidad,framerate_animacion,framerate_moviemiento) -> None:
        super().__init__()
        self.quieto_r = Auxliar.load_sprisheet(r"\characters\doom marine\idel.png", 8, 1, direcciones=True)
        self.quieto_l = Auxliar.load_sprisheet(r"\characters\doom marine\idel.png", 8, 1) 
        self.contador_salto = 0
        self.contador_caida = 0
        self.speed = velocidad
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.cooldown_dispario = 0
        self.direccion = DIRECCION_R
        self.animacion = self.quieto_r
        self.imagen = self.animacion[self.frame]
        self.mask = self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.posicion_inicial = y
        self.tiempo_trasncurrio_moviento = 0
        self.tiempo_trasncurrio_animacion = 0
        self.frame_rate_animacion = framerate_animacion
        self.frame_rate_movimiento = framerate_moviemiento
        self.disparando = False
        self.salto = False
        self.disparo = pygame.sprite.Group()

    def obtener_sprits(self,accion):
        
        match accion:
            case "caminar":
                if self.direccion == DIRECCION_R:
                    sprits = Auxliar.load_sprisheet(
                        r"\characters\doom marine\walk.png", 3, 1, direcciones=True)
                else:
                   sprits = Auxliar.load_sprisheet(
                       r"\characters\doom marine\walk.png", 3, 1)

            case "saltar":
                if self.direccion == DIRECCION_R:
                    sprits = Auxliar.load_sprisheet(
                        r"\characters\doom marine\jump.png", 4, 1, direcciones=True)
                else:
                    sprits = Auxliar.load_sprisheet(
                        r"\characters\doom marine\jump.png", 4, 1)

            case "disparar":
                if self.direccion == DIRECCION_R:
                    sprits = Auxliar.load_sprisheet(
                        r"\characters\doom marine\shoot.png", 5, 1, direcciones=True)
                else:
                    sprits = Auxliar.load_sprisheet(
                        r"\characters\doom marine\shoot.png", 5, 1)

        return sprits

    def caminar(self,direccion):

        # if self.direccion != direccion or (self.animacion != self.caminar_r or self.animacion != self.caminar_l):
            
            self.direccion = direccion

            if direccion == DIRECCION_R:

                    self.mover_x = self.speed

                    self.animacion = self.obtener_sprits("caminar")
                    
            else:

                    self.mover_x = -self.speed

                    self.animacion = self.obtener_sprits("caminar")
            
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

        self.animacion = self.obtener_sprits("saltar")


        print(self.mover_y)

    def disparar(self):
                
        self.animacion = self.obtener_sprits("disparar")            
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0

    def quieto(self):

        if self.animacion != self.quieto_r and self.animacion != self.quieto_l:

            if self.direccion == DIRECCION_R:

                self.animacion = self.quieto_r

            else:

                self.animacion = self.quieto_l

            self.mover_x = 0
            self.mover_y = 0
            self.frame = 0

    def landed(self):
        
        self.mover_y = 0
        self.contador_caida = 0
        self.contador_salto = 0
    
    def hit_head(self):

        self.mover_y *= -1

    def colicion_horizontal(self,objetos:list[Objeto],desplazamineto_y):

        coleccion_objetos = []

        for obj in objetos:

            if pygame.sprite.collide_mask(self,obj):
                
                if not self.salto:
                    if desplazamineto_y > 0:

                        self.rect.bottom = obj.rect.top 
                        self.landed()

                    # elif desplazamineto_y < 0 :

                    #     self.rect.top = obj.rect.bottom
                    #     self.hit_head()
                else:

                    if self.rect.top == obj.rect.bottom :

                        self.rect.top = obj.rect.bottom
                        self.hit_head()


                coleccion_objetos.append(obj)
            
        return coleccion_objetos

    def collide(self,objetos,desplazamiento_x):
        

        collide_obj = None
        for obj in objetos:

            if pygame.sprite.collide_mask(self,obj):
                
                collide_obj = obj
                break
            

        

        return collide_obj

    def control_horizontal(self,objeto):

        keys = pygame.key.get_pressed()
        
        colicion_izquierda = self.collide(objeto,-self.speed*2)
        colicion_derecha = self.collide(objeto,self.speed*2)

        if not keys[pygame.K_SPACE] and not keys[pygame.K_l] :

            if (keys[pygame.K_d] and not keys[pygame.K_a]) :

                self.caminar(DIRECCION_R)

            if (keys[pygame.K_a] and not keys[pygame.K_d]) :

                self.caminar(DIRECCION_L)

            if not keys[pygame.K_a] and not keys[pygame.K_d]:

                self.quieto()

            if  keys[pygame.K_a] and  keys[pygame.K_d]:

                self.quieto()

        self.colicion_horizontal(objeto,self.mover_y)

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

       

    def balas(self,screen):

        self.disparo.draw(screen)

        self.disparo.update()

    def do_moviento(self,delta_ms):


        self.mover_y += min(1, (self.contador_caida / FPS) * GRAVEDAD)

        self.tiempo_trasncurrio_moviento += delta_ms

        if self.tiempo_trasncurrio_moviento >= self.frame_rate_movimiento:

            if self.disparando and self.frame == 0:
                
                if self.cooldown_dispario == 0:

                    if self.direccion == DIRECCION_R:

                        self.disparo.add(Bala(self.rect.centerx + self.rect.size[0],self.rect.centery,self.direccion,"escopeta"))
                    
                    else:
                        
                        self.disparo.add(Bala(self.rect.centerx - self.rect.size[0],self.rect.centery,self.direccion,"escopeta"))

                    
                    self.cooldown_dispario = 20

            if self.mover_y > 1:

                self.salto = False


            self.tiempo_trasncurrio_moviento = 0

            self.rect.x += self.mover_x
            self.rect.y += self.mover_y

            if self.cooldown_dispario > 0:
                self.cooldown_dispario -= 1

        self.contador_caida += 1


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
        self.rect = self.imagen.get_rect(topleft = (self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.imagen)

    def draw(self,screen):

        if DEBUG:

            pygame.draw.rect(screen,ROJO,self.rect)

        self.balas(screen)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)

