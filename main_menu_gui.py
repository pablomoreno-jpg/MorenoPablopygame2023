import pygame
from constantes import*
from botones_gui import*


class Main_menu():

    def __init__(self) -> None:
        self.titulo = pygame.image.load(r"mis imagenes\extras\titulo.png")
        self.titulo = pygame.transform.scale(self.titulo,(self.titulo.get_width()*1.5,self.titulo.get_height()*1.4))
        self.rect_titulo = self.titulo.get_rect()
        self.rect_titulo.centerx = ANCHO_VENTANA / 2
        self.rect_titulo.y = 50
        self.boton_comenzar = Boton(ANCHO_VENTANA / 2,self.rect_titulo.centery + 200,"comenzar")
        self.boton_opcines = Boton(ANCHO_VENTANA / 2,self.boton_comenzar.rect.centery + 100,"opciones")
        self.boton_salir = Boton(ANCHO_VENTANA / 2,self.boton_opcines.rect.centery + 100,"salir")



    def draw(self,screen):

        
        fondo = pygame.image.load(r"mis imagenes\extras\fondo pausa.png")
        fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        screen.blit(fondo,fondo.get_rect())
        
        self.boton_comenzar.draw(screen)
        self.boton_opcines.draw(screen)
        self.boton_salir.draw(screen)     

        screen.blit(self.titulo,self.rect_titulo)

        