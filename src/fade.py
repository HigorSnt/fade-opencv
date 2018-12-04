# coding: utf-8

import cv2

# funcao responsavel por realizar o fade, utilizando combinação convexa
def fade(imagem1, imagem2):
	
	# porcentagem no qual a primeira imagem sera gravada
	porcentagem_imagem1 = 1
	
	# porcentagem no qual a segunda imagem sera gravada
	porcentagem_imagem2 = 0
	
	''' numero de imagens geradas, variavel utilizada para 
	    nomear as imagens de maneira diferente'''
	quantidade_imagens = 0
	
	while porcentagem_imagem2 <= 1:
		imagem_nova = porcentagem_imagem1 * imagem1 + porcentagem_imagem2 * imagem2
		
		porcentagem_imagem1 -= 0.2
		porcentagem_imagem2 += 0.2
		quantidade_imagens += 1
		
		cv2.imwrite("../output/imagem" + str(quantidade_imagens) + ".jpg", imagem_nova)
