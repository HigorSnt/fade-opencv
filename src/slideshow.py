import cv2
import os

# funcao responsavel por mostrar as imagens geradas na tela
def show():
	# lista com o nome dos arquivos de determinada pasta
	arquivos = os.listdir("../output")
	arquivos.sort()
	
	for imagem in arquivos:
		elemento = cv2.imread("../output/" + imagem)
		
		cv2.imshow("Imagem", elemento)
		cv2.waitKey(30)
	
	cv2.destroyAllWindows()
