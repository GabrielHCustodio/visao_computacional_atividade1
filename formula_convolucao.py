import numpy as np
import time
from scipy.signal import convolve2d

def executar_analise_pura():
    print("====================================================")
    print("   ANÁLISE PURA DO TEOREMA DA CONVOLUÇÃO (MATEMÁTICA) ")
    print("====================================================")
    
    # Criamos uma matriz sintética simulando uma imagem (ex: 500x500)
    # Isso evita depender do OpenCV e de arquivos externos para o teste
    tamanho_img = 500
    print(f"Gerando imagem computacional de {tamanho_img}x{tamanho_img} pixels...")
    img_simulada = np.random.rand(tamanho_img, tamanho_img)
    
    # Kernel de média grande (ex: 25x25) para pesar na convolução espacial pura
    tamanho_kernel = 25
    kernel = np.ones((tamanho_kernel, tamanho_kernel)) / (tamanho_kernel ** 2)
    
    print(f"Aplicando filtro com Kernel de {tamanho_kernel}x{tamanho_kernel}...\n")
    
    # --------------------------------------------------
    # 1. Domínio Espacial Puro (Matemático - Sem OpenCV)
    # --------------------------------------------------
    t_start = time.time()
    # Convolução clássica que varre a imagem pixel por pixel
    res_espacial = convolve2d(img_simulada, kernel, mode='same')
    t_espacial = time.time() - t_start
    print(f">> 1. Tempo no Domínio Espacial (Convolução Pura): {t_espacial:.6f} segundos")
    
    # --------------------------------------------------
    # 2. Domínio da Frequência (FFT)
    # --------------------------------------------------
    t_start = time.time()
    # Tamanho ideal para evitar efeitos de borda na FFT
    sz = (img_simulada.shape[0] + kernel.shape[0] - 1, img_simulada.shape[1] + kernel.shape[1] - 1)
    
    # Transforma ambos para a frequência
    img_fft = np.fft.fft2(img_simulada, s=sz)
    kernel_fft = np.fft.fft2(kernel, s=sz)
    
    # Multiplicação simples na frequência (O Teorema da Convolução)
    resultado_fft = img_fft * kernel_fft
    
    # Volta para o domínio espacial
    res_frequencia = np.fft.ifft2(resultado_fft).real
    
    # Ajusta o tamanho para ficar igual ao original
    f_h, f_w = res_frequencia.shape
    img_h, img_w = img_simulada.shape
    res_frequencia = res_frequencia[(f_h-img_h)//2 : (f_h+img_h)//2, (f_w-img_w)//2 : (f_w+img_w)//2]
    
    t_frequencia = time.time() - t_start
    print(f">> 2. Tempo no Domínio da Frequência (Multiplicação FFT): {t_frequencia:.6f} segundos")
    print("-" * 60)
    
    # --------------------------------------------------
    # Conclusão Teórica para o Vídeo
    # --------------------------------------------------
    print("ANÁLISE CIENTÍFICA DA FÓRMULA:")
    ganho = t_espacial / t_frequencia
    print(f"O Domínio da Frequência foi cerca de {ganho:.1f}x MAIS RÁPIDO!")

if __name__ == "__main__":
    executar_analise_pura()