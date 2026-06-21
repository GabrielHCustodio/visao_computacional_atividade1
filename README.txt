# Trabalho PDI - Processamento Digital de Imagens / Implementação de Técnicas de Pré-Processamento

Este repositório contém a implementação de quatro exercícios práticos desenvolvidos para a disciplina de Visão Computacional, abordando conceitos fundamentais de processamento de imagens.

## 🛠️ Estrutura do Projeto

A organização atual dos arquivos no diretório é a seguinte:

.
├── img/
│   ├── imagem.jpg
│   ├── fundo.jpg
│   └── pessoa.jpg
│
├── formula_convolucao.py
├── main.exe
├── main.py
├── q1_quantizacao.py
├── q2_subtracao.py
├── q3_high_boost.py
├── q4_convolucao.py
└── README.

---

## ⚙️ Pré-requisitos e Instalação

Certifique-se de ter o Python 3.12 (ou superior) instalado. Siga os passos abaixo para clonar o repositório, criar um ambiente virtual (venv) e instalar as dependências necessárias no Windows:

1. Clone este repositório e acesse a pasta:
   git clone https://github.com/GabrielHCustodio/visao_computacional_atividade1.git
   cd visao_computacional_atividade1

2. Crie e ative o ambiente virtual (venv):
   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências necessárias:
   pip install opencv-python numpy matplotlib scipy

---

## 🖼️ Preparação dos Dados (Imagens)

Para que os scripts funcionem corretamente, coloque as suas imagens de teste dentro da pasta img/. É esperado que as seguintes imagens sejam fornecidas com estes nomes exatos:
- imagem.jpg: Imagem colorida padrão para os testes dos Exercícios 1, 3 e 4.
- fundo.jpg: Imagem apenas do fundo (parede vazia) para o Exercício 2.
- pessoa.jpg: Imagem do seu corpo com o mesmo fundo para o Exercício 2.

Atenção à personalização e extensões dos arquivos:
Por padrão, os exercícios 1, 3 e 4 utilizam a mesma imagem base (imagem.jpg). Caso deseje adicionar e utilizar uma imagem diferente para um exercício específico (por exemplo, usar uma foto na Q3 diferente da Q1), ou se a sua imagem tiver outra extensão (como .png), o caminho deve ser alterado diretamente no código do script necessário (ex: q3_high_boost.py).

Exemplo de alteração no código:
# Como está no código original:
image_path = "img/imagem.jpg"

# Como deve ficar se você quiser usar uma foto exclusiva ou em PNG na Q3:
image_path = "img/imagem2.png"

---

## 🚀 Como Executar

A forma mais simples de testar e avaliar o projeto é executando o script principal, que abrirá um menu interativo no terminal. Com o ambiente virtual ativado, execute:

python main.py

Digite o número correspondente à funcionalidade desejada. As janelas gráficas com os resultados visuais serão geradas automaticamente pelo Matplotlib. 

> 💡 Nota: Para fechar um exercício e retornar ao menu principal do terminal, você deve fechar a janela de visualização de imagens que foi aberta.

---