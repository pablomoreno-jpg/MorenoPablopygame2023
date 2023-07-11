import pygame
from constantes import*
from botones_gui import*


class Main_menu():

    def __init__(self,salir) -> None:
        self.titulo = pygame.image.load(r"mis imagenes\extras\main menu\titulo.png")
        self.titulo = pygame.transform.scale(self.titulo,(self.titulo.get_width()*1.5,self.titulo.get_height()*1.4))
        self.rect_titulo = self.titulo.get_rect()
        self.rect_titulo.centerx = ANCHO_VENTANA / 2
        self.rect_titulo.y = 50
        self.salir = salir
        self.boton_comenzar = Boton(ANCHO_VENTANA / 2,self.rect_titulo.centery + 200,"comenzar",centrarx=True)
        self.boton_opcines = Boton(ANCHO_VENTANA / 2,self.boton_comenzar.rect.centery + 100,"opciones",centrarx= True)
        self.boton_salir = Boton(ANCHO_VENTANA / 2,self.boton_opcines.rect.centery + 100,"salir",centrarx= True)


    def update(self,screen):

        comenzar = False

        if self.boton_comenzar.draw(screen):
            comenzar = True

        if self.boton_opcines.draw(screen):
            print("opciones")

        if self.boton_salir.draw(screen):   
            self.salir = True

        return comenzar
        

    def draw(self,screen) -> bool|bool:

        
        fondo = pygame.image.load(r"mis imagenes\extras\fondo pausa.png")
        fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        screen.blit(fondo,fondo.get_rect())

        comenzar = self.update(screen)

        screen.blit(self.titulo,self.rect_titulo)

        return comenzar,self.salir


class Pausa():

    def __init__(self, salir) -> None:

        self.titulo = pygame.image.load(r"mis imagenes\extras\pausa\pusa.png")
        self.titulo = pygame.transform.scale(self.titulo,(self.titulo.get_width()*1.5,self.titulo.get_height()*1.4))
        self.rect_titulo = self.titulo.get_rect()
        self.rect_titulo.x = 100
        self.rect_titulo.y = 50
        self.salir = salir
        self.boton_continuar = Boton(100,self.rect_titulo.y +200,"continuar")
        self.boton_opcines = Boton(100,self.boton_continuar.rect.y +100,"opciones")
        self.boton_salir_menu = Boton(100,self.boton_opcines.rect.y +100,"salir menu")
        self.boton_salir = Boton(100,self.boton_salir_menu.rect.y +100,"salir")


    def update(self,screen):

        pausa = True

        if self.boton_continuar.draw(screen):
            pausa = False

        if self.boton_opcines.draw(screen):
            print("opciones")

        if self.boton_salir_menu.draw(screen):
            print("salir al menu")

        if self.boton_salir.draw(screen):   
            self.salir = False

        return pausa

    def draw(self,screen) -> bool|bool :

        
        fondo = pygame.image.load(r"mis imagenes\extras\fondo pausa.png")
        fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        screen.blit(fondo,fondo.get_rect())
        
        pausa = self.update(screen)

        screen.blit(self.titulo,self.rect_titulo)

        return pausa,self.salir