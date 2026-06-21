import cv2
import numpy as np
import time

def executar_q4():
    print("--- Questão 4: Teorema da Convolução ---")
    
    image_path = "./img/imagem.jpg"
    tamanho_kernel = 151 # Kernel grande fixo para dar diferença gritante de tempo
    
    img_color = cv2.imread(image_path)
    if img_color is None:
        print(f"Erro: Não encontrei a imagem em '{image_path}'!")
        return
        
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    h, w = img.shape
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.float32) / (tamanho_kernel ** 2)
    
    # 1. Domínio Espacial
    t_start = time.time()
    res_espacial = cv2.filter2D(img, -1, kernel)
    t_espacial = time.time() - t_start
    
    # 2. Domínio da Frequência (FFT)
    t_start = time.time()
    dft_h = cv2.getOptimalDFTSize(h + tamanho_kernel - 1)
    dft_w = cv2.getOptimalDFTSize(w + tamanho_kernel - 1)
    
    img_dft = np.fft.fft2(img, s=(dft_h, dft_w))
    kernel_dft = np.fft.fft2(kernel, s=(dft_h, dft_w))
    
    resultado_dft = img_dft * kernel_dft
    res_frequencia = np.fft.ifft2(resultado_dft).real[:h, :w]
    res_frequencia = np.clip(res_frequencia, 0, 255).astype(np.uint8)
    t_frequencia = time.time() - t_start
    
    print(f"\n>> Tempo no Domínio Espacial: {t_espacial:.6f} segundos")
    print(f">> Tempo no Domínio da Frequência (FFT): {t_frequencia:.6f} segundos")
    print("-" * 50)
    
if __name__ == "__main__":
    executar_q4()