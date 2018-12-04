# coding: utf-8

import cv2
import numpy as np
from fade import fade
from mostra_imagens import show

imagem1 = cv2.imread("../input/deadpool.jpg")
imagem2 = cv2.imread("../input/mario.jpg")

# chamando o responsavel por realizar o fade
fade(imagem1, imagem2)

# mostrando o resultado na tela
show()
