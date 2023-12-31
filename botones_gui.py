import pygame



IMGAENES_BOTONES = {"comenzar":pygame.image.load(r"mis imagenes\extras\main menu\opcion 1.png"),
                    "continuar":pygame.image.load(r"mis imagenes\extras\pausa\opcion 1.png"),
                    "opciones":pygame.image.load(r"mis imagenes\extras\opcion 2.png"),
                    "salir menu":pygame.image.load(r"mis imagenes\extras\pausa\opcion 4.png"),
                    "salir":pygame.image.load(r"mis imagenes\extras\opcion 3.png"),
                    "01":pygame.image.load(r"mis imagenes\extras\elegir niveles\01.png"),
                    "02":pygame.image.load(r"mis imagenes\extras\elegir niveles\02.png"),
                    "03":pygame.image.load(r"mis imagenes\extras\elegir niveles\03.png"),
                    "04":pygame.image.load(r"mis imagenes\extras\elegir niveles\04.png"),
                    "05":pygame.image.load(r"mis imagenes\extras\elegir niveles\05.png")}


class Boton():
    def __init__(self,x,y,nombre_boton,centrarx = False) -> None:
        

        self.imagen = IMGAENES_BOTONES[nombre_boton]
        self.rect = self.imagen.get_rect()
        self.centrarx = centrarx
        self.rect.x= x - self.centrar_x()
        self.rect.y = y 
        self.click = False

    def centrar_x(self):

        ancho = 0

        if self.centrarx:

            ancho = self.imagen.get_width() / 2

        return ancho

    def draw(self,screen):
        
        accion = False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            
           if pygame.mouse.get_pressed()[0] == 1 and self.click == False:

               self.click = True
               accion = True

        if pygame.mouse.get_pressed()[0] == 0:

            self.click = False

        screen.blit(self.imagen,(self.rect.x,self.rect.y))
       
        return accion
