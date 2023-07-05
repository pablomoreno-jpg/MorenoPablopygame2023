import	pygame
from constantes import*


class BarraSalud():

    def __init__(self,x,y,barra_salud,salud_maxima,escudo,escudo_maximo) -> None:
        
        self.x = x
        self.y = y
        self.salud = barra_salud
        self.salud_maxima = salud_maxima



    def draw(self,vida_actual,escudo_actual ,screen):
        
        self.salud =  vida_actual
        #calculo para bajar la barra de salud
        ratio_salud = self.salud / self.salud_maxima
        #salud
        pygame.draw.rect(screen,ROJO,(self.x+2,self.y+30,179,15))
        pygame.draw.rect(screen,VERDE,(self.x+2,self.y+30,179*ratio_salud,15))
        #escudo
  
            
        pygame.draw.rect(screen,AZUL,(self.x+5,self.y+5,escudo_actual,15))

        barra = pygame.image.load(r"C:\Users\pablo\OneDrive\Escritorio\doom's gate\mis imagenes\extras\barra vida y escudo.png")
        rect_barra = barra.get_rect()
        rect_barra.x = self.x
        rect_barra.y = self.y

        screen.blit(barra,rect_barra)
        
        
        pass