from typing import Any
import pygame
from pygame.sprite import _Group
from constantes import*
from auxiliar import*



class grnada(pygame.sprite.Sprite):

    def __init__(self, *groups: _Group) -> None:
        super().__init__(*groups)