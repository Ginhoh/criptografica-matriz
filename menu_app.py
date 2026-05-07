import time 
gramatica = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, 
             "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, 
             "V":22, "W":23, "X":24, "Y":25, "Z":26, "Ã":27, "Á":28, "Ó":29, "Ô":30, "Ç":31, 
             "#":32, "?":33 , "!":34, ".":35, ";":36,"0":37, "1":38, "2":39, "3":40,"4":41,
             "5":42, "6":43, "7":44, "8":45, "9":46, ",":47}

def criptografar(texto):
    if len(texto) % 2 != 0: #Caso o número de caracteres seja ímpar, adiciona-se um caractere de espaço no final da string
        texto += "#"
    matriz = [  #Matriz que estará sendo preenchida com os números inteiros correspondentes a cada letra da string
        [],
        []
        ]
    matriz_criptogradora = [ #Matriz de criptografia
        [1,3],
        [2, 7]
    ]
    
    #Preenchendo a primeira matriz com a primeira metade da string
    for i in range(0, int(len(texto)/2)):
            matriz[0].append(gramatica[texto[i]])

    #Preenchendo a primeira matriz com a segunda metade da string
    for i in range(int(len(texto)/2), len(texto)):
            matriz[1].append(gramatica[texto[i]])
    
    
    #multiplicando (convertendo) as matrizes
    matriz_resultante = [
        [],
        []
    ]
    
    for i in range(0, 2): #Intervalos associados ao número de linhas e colunas das matrizes
        for j in range(0, len(matriz[0])):
            matriz_resultante[i].append(matriz_criptogradora[i][0] * matriz[0][j] + matriz_criptogradora[i][1] * matriz[1][j])

    print("Mensagem Criptografada: ")
    for i in matriz_resultante:
        for j in i:
            print(j, end=' ')

def descriptografar():
    texto = input("\nDigite os números inteiros separados por espaço: ")
    matriz_descriptogradora = [
        [7, -3],
        [-2, 1]
    ]
    numeros = [int(x) for x in texto.split()]
    print(f"Números digitados: {numeros}")

    matriz = [
         [],
         []
    ]
    
    for i in range(0, int(len(numeros)/2)):
            matriz[0].append(numeros[i])

    for i in range(int(len(numeros)/2), len(numeros)):
            matriz[1].append(numeros[i])
            
    
    # #multiplicando (convertendo) as matrizes
    matriz_resultante = [
        [],
        []
    ]
    for i in range(0, 2): #Intervalos associados ao número de linhas e colunas das matrizes
        for j in range(0, len(matriz[0])):
            matriz_resultante[i].append(matriz_descriptogradora[i][0] * matriz[0][j] + matriz_descriptogradora[i][1] * matriz[1][j])

    print("\nMensagem Decodificada:\n ")
    mensagem_decodificada = ''
    for i in matriz_resultante:
        for j in i:
            for chave, valor in gramatica.items():
                if j == valor:
                   mensagem_decodificada += chave  # Saída sem espaço entre as letras

    print(mensagem_decodificada.replace("#", " ")) #Substitui o caractere de espaço pelo caractere de espaço real


while True: #INICIALIZA O MENU
     print("")
     print("-"*30)
     print("BEM VINDO AO NOSSO SISTEMA DE CRIPTOGRAFIA E DESCRIPTOGRAFIA \n POR FAVOR ESCOLHA UMA DAS OPÇÕES ABAIXO:")
     print("1 - CRIPTOGRAFIA\n2 - DESCRIPTOGRAFIA\n3 - SAIR")
     print("-"*30)

     opcao = int(input("DIGITE A OPÇÃO DESEJADA: ")) #RECEBE A OPÇÃO ESCOLHIDA PELO USUARIO
     if opcao == 1: #VALIDA CADA OPÇÂO DA 1 A 3
        texto = str(input("Digite algo: ")).upper().replace(" ", "#")
        criptografar(texto)
     elif opcao == 2:
          descriptografar()
     elif opcao == 3:
          print("Encerrando o programa...")
          time.sleep(0.3)
          break; #ENCERRA O LOOPING
     else:
        print("OPÇÃO INVALIDA!\nDIGITE UM NUMERO VALIDO")