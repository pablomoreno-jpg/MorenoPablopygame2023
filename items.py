from typing import Any
import pygame
from constantes import*
from auxiliar import*
from jugador import*

ITEMS = {"escopeta":Auxliar.load_sprisheet(r"\items\armas.png", 1, 3)[0],
        "bazuca":Auxliar.load_sprisheet(r"\items\armas.png", 1, 3)[1],
        "plasma":Auxliar.load_sprisheet(r"\items\armas.png", 1, 3)[2],
        "posion": Auxliar.load_sprisheet(r"\items\posion vida.png", 4, 1)[-1],
         "botiquin pequeño": Auxliar.load_sprisheet(r"\items\vida.png", 1, 2)[0],
         "botiquin": Auxliar.load_sprisheet(r"\items\vida.png", 1, 2)[1],
         "escudo pequeño": Auxliar.load_sprisheet(r"\items\escudo.png", 2, 2),
         "escudo": Auxliar.load_sprisheet(r"\items\escudo max.png", 2, 1)[0],
         "granadas": Auxliar.load_sprisheet(r"\items\municion.png",2,2)[0],
         "misil unit": Auxliar.load_sprisheet(r"\items\municion.png", 3, 2)[1],
         "misiles": Auxliar.load_sprisheet(r"\items\municion.png", 3, 2)[2],
         "misiles y granadas": Auxliar.load_sprisheet(r"\items\municion.png", 3, 2)[3],
         "punto_2": Auxliar.load_sprisheet(r"\items\puntos.png", 3, 2)[1],
         "puntos_5": Auxliar.load_sprisheet(r"\items\puntos.png", 3, 2)[3],
         "puntos_10": Auxliar.load_sprisheet(r"\items\puntos.png", 3, 2)[5]}

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

                if player.salud < player.self_maxima:

                    player.salud += 5
                    self.kill()

            elif self.tipo_item == "botiquin pequeño":

                if player.salud < player.self_maxima:

                    player.salud += 15
                    self.kill()

            elif self.tipo_item == "botiquin":

                if player.salud < player.self_maxima:

                    player.salud += 25
                    self.kill()


            elif self.tipo_item == "escudo pequeño":

                if player.escudo < player.escudo_maximo:

                    player.escudo += 5
                    self.kill()

            elif self.tipo_item == "escudo":

                if player.escudo < player.escudo_maximo:

                    player.escudo += 15
                    self.kill()

            elif self.tipo_item == "granadas":

                if player.grandas < player.grandas_maximas:

                    player.grandas += 2

                    self.kill()

            elif self.tipo_item == "misil unit":

                if player.munision_misiles < player.misiles_maximos:

                    player.munision_misiles += 1

                    self.kill()

            elif self.tipo_item == "misiles":

                if player.munision_misiles < player.misiles_maximos:

                    player.munision_misiles += 5

                    self.kill()

            elif self.tipo_item == "misiles y granadas":

                if player.munision_misiles < player.misiles_maximos and player.grandas < player.grandas_maximas:

                    player.munision_misiles += 5
                    player.grandas += 2
                    self.kill()

            elif self.tipo_item == "escopeta":

                player.arma = "escopeta"
                player.cooldown_maximo = 20
                self.kill()
