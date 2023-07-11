from typing import Any
import pygame
from constantes import*
from auxiliar import*


class Bala(pygame.sprite.Sprite):

    def __init__(self,x,y,direccion,tipo) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.tipo = tipo
        self.direccion = direccion
        self.image = self.direccion_bala()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def obtener_bala(self):

        match self.tipo:

            case "default":
                
                imagen = Auxliar.load_sprisheet(r"{0}\bullet.png".format(PAHT_PROYECTILES),columnas=2,filas=2)[0]

                imagen = pygame.transform.scale2x(imagen)

                self.speed = 12

            case "escopeta":
                
                imagen = Auxliar.load_sprisheet(r"{0}\bullet.png".format(PAHT_PROYECTILES),columnas=2,filas=2)[1]

                self.speed = 8

            case "plasma":
                
                imagen = Auxliar.load_sprisheet(r"{0}\bullet.png".format(PAHT_PROYECTILES),columnas=2,filas=2)[2]

                self.speed = 17


            case "energia":
              
                imagen = Auxliar.load_sprisheet(r"{0}\bullet.png".format(PAHT_PROYECTILES),columnas=2,filas=2)[3]

                self.speed = 13

        return imagen

    def direccion_bala(self):

        imagen = self.obtener_bala()

        if self.direccion == DIRECCION_R:

            imagen = pygame.transform.flip(imagen,True,False)

        return imagen
    
    def update(self,player):
        
        if self.direccion == DIRECCION_R:

            self.rect.x += self.speed

        else:

            self.rect.x -= self.speed

        if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            self.kill()


        