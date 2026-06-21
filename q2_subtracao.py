import cv2
import numpy as np
import matplotlib.pyplot as plt

def executar_q2():
    print("--- Questão 2: Subtração de Fundo e Detecção ---")
    
    image_path_fundo = "./img/fundo.jpg"
    image_path_corpo = "./img/pessoa.jpg"
    limiar = 30 
    
    img_color_fundo = cv2.imread(image_path_fundo)
    img_color_corpo = cv2.imread(image_path_corpo)
    
    if img_color_fundo is None or img_color_corpo is None:
        print("Erro: Verifique se 'fundo.jpg' e 'corpo.jpg' estão na pasta 'imagens'!")
        return
        
    bg = cv2.cvtColor(img_color_fundo, cv2.COLOR_BGR2GRAY)
    fg = cv2.cvtColor(img_color_corpo, cv2.COLOR_BGR2GRAY)
    
    subtracao = cv2.absdiff(bg, fg)
    _, binaria = cv2.threshold(subtracao, limiar, 255, cv2.THRESH_BINARY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    binaria_limpa = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel)
    
    contornos, _ = cv2.findContours(binaria_limpa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Converte para RGB para o Matplotlib plotar as cores certas
    img_resultado = cv2.cvtColor(img_color_corpo, cv2.COLOR_BGR2RGB)
    
    if contornos:
        maior_contorno = max(contornos, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(maior_contorno)
        # Retângulo Vermelho em RGB: (255, 0, 0)
        cv2.rectangle(img_resultado, (x, y), (x + w, y + h), (255, 0, 0), 3)
    
    # Plota tudo usando o Matplotlib (Evita o bug do cv2.imshow)
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.title("1. Subtracao Absoluta")
    plt.imshow(subtracao, cmap='gray')
    
    plt.subplot(1, 3, 2)
    plt.title("2. Resultado Binarizado")
    plt.imshow(binaria_limpa, cmap='gray')
    
    plt.subplot(1, 3, 3)
    plt.title("3. Corpo Detectado")
    plt.imshow(img_resultado)
    
    print("Feche a janela do gráfico para retornar ao menu.")
    plt.show()

if __name__ == "__main__":
    executar_q2()