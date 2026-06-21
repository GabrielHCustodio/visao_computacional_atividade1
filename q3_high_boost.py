import cv2
import numpy as np
import matplotlib.pyplot as plt

def executar_q3():
    print("--- Questão 3: Filtro High-Boost Customizado ---")
    
    image_path = "./img/imagem.jpg"
    A = 1.2 # Fator de ganho fixo para o High-Boost
    
    img_color = cv2.imread(image_path)
    if img_color is None:
        print(f"Erro: Não encontrei a imagem em '{image_path}'!")
        return
        
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    borrada = cv2.GaussianBlur(img, (5, 5), 0)
    passa_alta = cv2.subtract(img, borrada)
    
    img_f = img.astype(np.float32)
    borrada_f = borrada.astype(np.float32)
    high_boost_f = (A * img_f) - borrada_f
    high_boost = np.clip(high_boost_f, 0, 255).astype(np.uint8)
    
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1), plt.title("Original"), plt.imshow(img, cmap='gray')
    plt.subplot(1, 3, 2), plt.title("Passa-Alta Puro"), plt.imshow(passa_alta, cmap='gray')
    plt.subplot(1, 3, 3), plt.title(f"High-Boost (A={A})"), plt.imshow(high_boost, cmap='gray')
    
    print("Feche a janela do gráfico para retornar ao menu.")
    plt.show()

if __name__ == "__main__":
    executar_q3()