import cv2
import numpy as np
import matplotlib.pyplot as plt

def executar_q1():
    print("--- Questão 1: Quantização de Tons de Cinza ---")
    
    # Caminho fixo direto para a pasta imagens
    image_path = "./img/imagem.jpg"
    
    img_color = cv2.imread(image_path)
    if img_color is None:
        print(f"Erro: Não foi possível encontrar a imagem em '{image_path}'!")
        return
    
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    # Reduz de 256 para 64 tons (agrupando de 4 em 4)
    img_quantizada = (img_gray // 4) * 4
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original (Até 256 tons)")
    plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
    
    plt.subplot(1, 2, 2)
    plt.title("Quantizada (Até 64 tons)")
    plt.imshow(img_quantizada, cmap='gray', vmin=0, vmax=255)
    
    print("Feche a janela do gráfico para retornar ao menu.")
    plt.show()

if __name__ == "__main__":
    executar_q1()