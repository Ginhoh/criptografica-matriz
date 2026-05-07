# criptografica-matriz

# Criptografia com Matrizes: Um Projeto Acadêmico

## Introdução

Este projeto implementa um sistema de criptografia baseado em operações matriciais, inspirado no conceito de criptografia de Hill. O programa utiliza uma matriz de criptografia 2x2 para transformar mensagens de texto em sequências numéricas criptografadas e vice-versa. Este trabalho foi desenvolvido como parte de um estudo acadêmico sobre matemática de matrizes e suas aplicações em criptografia.

## Mapeamento de Caracteres

O programa utiliza um dicionário para mapear cada letra do alfabeto e o espaço para números inteiros:

```python
gramatica = {
    "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,
    "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
    "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26, "#":27
}
```

- As letras A-Z são mapeadas para os números 1-26
- O espaço é representado pelo caractere "#" e mapeado para 27

## Funcionalidades Principais

### Função `criptografar(texto)`

Esta função é responsável por criptografar uma mensagem de texto usando operações matriciais.

#### Passos da Criptografia:

1. **Preparação do Texto:**
   - Converte a entrada para maiúsculas
   - Substitui espaços por "#"
   - Se o comprimento for ímpar, adiciona um "#" no final para garantir que seja par

2. **Divisão em Matriz:**
   - Cria uma matriz 2xN onde N é metade do comprimento do texto
   - A primeira linha contém os primeiros N caracteres mapeados
   - A segunda linha contém os próximos N caracteres mapeados

3. **Matriz de Criptografia:**
   ```
   [1, 3]
   [2, 7]
   ```

4. **Multiplicação Matricial:**
   - Para cada coluna da matriz de texto, calcula:
     - Linha 1: (1 × valor_linha1) + (3 × valor_linha2)
     - Linha 2: (2 × valor_linha1) + (7 × valor_linha2)

5. **Saída:**
   - Imprime os números resultantes separados por espaços

#### Exemplo:
Para o texto "AB":
- Mapeamento: A=1, B=2
- Matriz: [[1], [2]]
- Criptografia: [[1×1 + 3×2], [2×1 + 7×2]] = [[7], [16]]
- Saída: 7 16

### Função `descriptografar()`

Esta função descriptografa uma sequência de números de volta para o texto original.

#### Passos da Descriptografia:

1. **Entrada:**
   - Recebe uma string de números inteiros separados por espaços

2. **Matriz de Descriptografia:**
   ```
   [7, -3]
   [-2, 1]
   ```
   Esta é a matriz inversa da matriz de criptografia.

3. **Divisão em Matriz:**
   - Organiza os números em uma matriz 2xN

4. **Multiplicação Matricial:**
   - Aplica a matriz inversa para recuperar os valores originais

5. **Mapeamento Inverso:**
   - Converte os números de volta para letras usando o dicionário `gramatica`
   - Substitui "#" por espaços

6. **Saída:**
   - Imprime a mensagem descriptografada

## Fundamentos Matemáticos

### Criptografia de Hill

Este programa implementa uma variante simplificada da criptografia de Hill, que usa multiplicação matricial para criptografar mensagens.

### Matriz de Criptografia

A matriz usada é:
```
C = [1, 3]
    [2, 7]
```

Para criptografar um par de valores [x, y], calcula-se:
```
[x'] = [1, 3] [x]
[y']   [2, 7] [y]
```

Ou equivalentemente:
```
x' = 1x + 3y
y' = 2x + 7y
```

### Matriz Inversa

A matriz de descriptografia é a inversa de C:
```
C⁻¹ = [7, -3]
      [-2, 1]
```

Para verificar: C × C⁻¹ deve resultar na matriz identidade.

### Determinantes e Inversibilidade

O determinante de C é: (1×7) - (3×2) = 7 - 6 = 1

Como o determinante é 1 (não zero), a matriz é inversível.

## Como Usar o Programa

1. Execute o programa Python
2. Digite uma mensagem para criptografar
3. O programa exibirá a mensagem criptografada como números
4. Para descriptografar, digite os números separados por espaços
5. O programa exibirá a mensagem original

## Limitações

- Funciona apenas com letras maiúsculas e espaços
- Requer comprimento par (adiciona # se necessário)
- Não implementa criptografia modular (os valores podem ser grandes)
- Não trata caracteres especiais ou minúsculas

## Aplicações Acadêmicas

Este projeto demonstra:
- Operações matriciais básicas (multiplicação)
- Conceitos de matrizes inversas
- Aplicações práticas da álgebra linear
- Princípios fundamentais da criptografia simétrica

## Conclusão

Este programa serve como uma introdução prática aos conceitos de criptografia matricial, ilustrando como operações matemáticas simples podem ser usadas para proteger informações. Embora simplificado, demonstra os princípios fundamentais que formam a base de sistemas de criptografia mais complexos.
