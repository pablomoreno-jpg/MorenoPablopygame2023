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
        self.comenzar = False
        self.boton_comenzar = Boton(ANCHO_VENTANA / 2,self.rect_titulo.centery + 200,"comenzar",centrarx=True)
        self.boton_opcines = Boton(ANCHO_VENTANA / 2,self.boton_comenzar.rect.centery + 100,"opciones",centrarx= True)
        self.boton_salir = Boton(ANCHO_VENTANA / 2,self.boton_opcines.rect.centery + 100,"salir",centrarx= True)

    def update(self,screen):

        if self.boton_comenzar.draw(screen):
            
            self.comenzar = True

        if self.boton_opcines.draw(screen):
            print("opciones")

        if self.boton_salir.draw(screen):   
            self.salir = False

        

    def draw(self,screen) -> bool|bool:

        
        fondo = pygame.image.load(r"mis imagenes\extras\fondo pausa.png")
        fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        screen.blit(fondo,fondo.get_rect())

        comenzar = self.update(screen)

        screen.blit(self.titulo,self.rect_titulo)

        return self.comenzar,self.salir


class Niveles():

    def __init__(self) -> None:
        self.imagen_titulo = pygame.image.load(r"mis imagenes\extras\elegir niveles\titulo.png")
        self.rect_titulo = self.imagen_titulo.get_rect()
        self.rect_titulo.centerx = ANCHO_VENTANA / 2
        self.rect_titulo.y = 50
        self.nombre_nivel = "prueba"
        self.boto_01 = Boton(100,self.rect_titulo.y +200,"01")
        self.boto_02 = Boton(100,self.boto_01.rect.y +50,"02")
        self.boto_03 = Boton(100,self.boto_02.rect.y +50,"03")
        self.boto_04 = Boton(100,self.boto_03.rect.y +50,"04")
        self.boto_05 = Boton(100,self.boto_04.rect.y +50,"05")
        
    def update(self,screen):

        nivel_elegido = False

        if self.boto_01.draw(screen):

            self.nombre_nivel = "nivel 1"
            nivel_elegido = True

        if self.boto_02.draw(screen):

            self.nombre_nivel = "nivel 2"
            nivel_elegido = True

        if self.boto_03.draw(screen):

            self.nombre_nivel = "nivel 3"
            nivel_elegido = True

        if self.boto_04.draw(screen):

            self.nombre_nivel = "nivel 4"
            nivel_elegido = True

        if self.boto_05.draw(screen):

            self.nombre_nivel = "nivel 5"
            nivel_elegido = True

        return nivel_elegido

    def draw(self,screen):
        

        fondo = pygame.image.load(r"mis imagenes\extras\fondo pausa.png")
        fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        screen.blit(fondo,fondo.get_rect())

        flag = self.update(screen)

        screen.blit(self.imagen_titulo,self.rect_titulo)

        return flag


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