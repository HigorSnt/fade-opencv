#coding: utf-8

import cv2
import numpy as np
import os

# funcao responsavel por mostrar as imagens geradas na tela
def show():
	# lista com o nome dos arquivos de determinada pasta
	arquivos = os.listdir("../output")
	arquivos.sort()

	for posicao,imagem in enumerate(arquivos):
		elemento = cv2.imread("../output/" + imagem)
		
		cv2.imshow("Imagem " + str(posicao + 1), elemento)
		cv2.waitKey(500)
		cv2.destroyAllWindows()
