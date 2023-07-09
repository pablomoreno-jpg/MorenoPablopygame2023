import pygame
from constantes import*
from auxiliar import*



# def get_block(phat_bloques:str,size:int,pos_x:int,pos_y:int) -> pygame:

#     imagen = pygame.image.load(phat_bloques).convert_alpha()
#     superfice = pygame.Surface((size,size),pygame.SRCALPHA, 32)
#     rect = pygame.Rect(pos_x,pos_y,size,size)
    
#     superfice.blit(imagen,(0,0), rect)

#     return superfice


class Objeto(pygame.sprite.Sprite):

    def __init__(self,x,y,tamaño,path) -> None:
        super().__init__()
        self.rect = pygame.Rect(x,y,tamaño,tamaño)
        self.imagen = pygame.Surface((tamaño,tamaño),pygame.SRCALPHA)
        self.size = tamaño
        self.ruta = path

    def draw(self,screen):

        if DEBUG:
            
            pygame.draw.rect(screen,VERDE,self.rect)
        
        else:
            screen.blit(self.imagen,(self.rect.x, self.rect.y))
        
            screen.blit(self.imagen,self.rect)



class Plataforma(Objeto):

    def __init__(self, x, y,tamaño,path,image_indec,columnas = 0,filas = 0) -> None:

        super().__init__(x, y, tamaño,path)
        imagen = Auxliar.load_sprisheet(path,columnas=24,filas=12)[image_indec]
        self.pos_x = tamaño * columnas
        self.pos_y = tamaño * filas
        self.imagen.blit(imagen, (0, 0))
        self.mask = pygame.mask.from_surface(self.imagen)
        self.path = path

        
        

