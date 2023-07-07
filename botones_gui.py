import pygame



IMGAENES_BOTONES = {"comenzar":pygame.image.load(r"mis imagenes\extras\opcion 1.png"),
                    "opciones":pygame.image.load(r"mis imagenes\extras\opcion 2.png"),
                    "salir":pygame.image.load(r"mis imagenes\extras\opcion 3.png")}


class Boton():
    def __init__(self,x,y,nombre_boton) -> None:
        
        self.imagen = IMGAENES_BOTONES[nombre_boton]
        self.rect = self.imagen.get_rect()
        self.rect.centerx = x
        self.rect.y = y 
        self.click = False

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
