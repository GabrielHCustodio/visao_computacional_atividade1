import sys

try:
    import q1_quantizacao
    import q2_subtracao
    import q3_high_boost
    import q4_convolucao
    import formula_convolucao
except ImportError as e:
    print(f"Erro ao importar os scripts das questões: {e}")
    print("Certifique-se de que todos os arquivos (.py) estão na mesma pasta.")
    sys.exit(1)

def menu():
    while True:
        print("\n=======================================================")
        print("          TECNICAS DE PRE-PROCESSAMENTO - MENU PRINCIPAL             ")
        print("=======================================================")
        print("1 - Quantização de Tons de Cinza (Q1)")
        print("2 - Subtração de Fundo e Detecção de Corpo (Q2)")
        print("3 - Filtro High-Boost vs Passa-Alta (Q3)")
        print("4 - Teorema da Convolução - OpenCV (Q4)")
        print("5 - Análise Pura da Fórmula da Convolução (Bônus Teórico)")
        print("0 - Sair")
        print("=======================================================")
        
        opcao = input("Escolha a funcionalidade desejada: ")
        
        if opcao == "1":
            q1_quantizacao.executar_q1()
        elif opcao == "2":
            q2_subtracao.executar_q2()
        elif opcao == "3":
            q3_high_boost.executar_q3()
        elif opcao == "4":
            q4_convolucao.executar_q4()
        elif opcao == "5":
            formula_convolucao.executar_analise_pura()
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()