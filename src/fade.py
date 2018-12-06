import cv2

# funcao responsavel por realizar o fade, utilizando combinacao convexa
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
		
		porcentagem_imagem1 -= 0.02
		porcentagem_imagem2 += 0.02
		quantidade_imagens += 1
		
		cv2.imwrite("../output/imagem" + "{:02d}".format(quantidade_imagens) + ".jpg", imagem_nova)
