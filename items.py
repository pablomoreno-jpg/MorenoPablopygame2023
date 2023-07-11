from typing import Any
import pygame
from constantes import*
from auxiliar import*
from jugador import*

ITEMS = {"escopeta":Auxliar.load_sprisheet(r"{0}\items\armas.png".format(PHAT_RECURSOS), 1, 3)[0],
        "plasma":Auxliar.load_sprisheet(r"{0}\items\armas.png".format(PHAT_RECURSOS), 1, 3)[1],
        "posion": Auxliar.load_sprisheet(r"{0}\items\posion vida.png".format(PHAT_RECURSOS), 4, 1)[-1],
         "botiquin pequeño": Auxliar.load_sprisheet(r"{0}\items\vida.png".format(PHAT_RECURSOS), 1, 2)[0],
         "botiquin": Auxliar.load_sprisheet(r"{0}\items\vida.png".format(PHAT_RECURSOS), 1, 2)[1],
         "escudo pequeño": Auxliar.load_sprisheet(r"{0}\items\escudo.png".format(PHAT_RECURSOS), 2, 2)[3],
         "escudo": Auxliar.load_sprisheet(r"{0}\items\escudo max.png".format(PHAT_RECURSOS), 2, 1)[0],
         "punto_2": Auxliar.load_sprisheet(r"{0}\items\puntos.png".format(PHAT_RECURSOS), 3, 2)[1],
         "puntos_5": Auxliar.load_sprisheet(r"{0}\items\puntos.png".format(PHAT_RECURSOS), 3, 2)[3],
         "puntos_10": Auxliar.load_sprisheet(r"{0}\items\puntos.png".format(PHAT_RECURSOS), 3, 2)[5]}

class Items(pygame.sprite.Sprite):

    def __init__(self,x,y,item_tipo) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.tipo_item = item_tipo
        self.image = ITEMS[self.tipo_item]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TAM_BLOQUE // 2, y + (TAM_BLOQUE - self.image.get_height()))

    def update(self, player: Jugador) -> None:

        if pygame.sprite.collide_rect(self, player):

            if self.tipo_item == "posion":

                if player.salud < player.salud_maxima:

                    player.salud += 5

            elif self.tipo_item == "botiquin pequeño":

                if player.salud < player.salud_maxima:

                    player.salud += 15

            elif self.tipo_item == "botiquin":

                if player.salud < player.salud_maxima:

                    player.salud += 25

            elif self.tipo_item == "escudo pequeño":

                if player.escudo < player.escudo_maximo:

                    player.escudo += 5
                

            elif self.tipo_item == "escudo":

                if player.escudo < player.escudo_maximo:

                    player.escudo += 15

            elif self.tipo_item == "escopeta":

                player.arma = "escopeta"
                player.cooldown_maximo = 20

            elif self.tipo_item == "plasma":

                player.arma = "plasma"
                player.cooldown_maximo = 3
        
            #en caso de sobrepasar las barrras maximas
            if player.salud > player.salud_maxima:

                diferencia = player.salud -player.salud_maxima

                player.salud -= diferencia

            if player.escudo > player.escudo_maximo:

                diferencia = player.escudo - player.escudo_maximo

                player.escudo -= diferencia

            self.kill()

    def draw(self,screen):

        screen.blit(self.image,self.rect)

        pass