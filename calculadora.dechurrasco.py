# 1) solicitar o número de convidados
# usamos o int por que convidados deve ser um número inteiro
convidados = int(input('Digite o número de convidados: '))

# 2) criar uma função para calcular a quantidade total de bebidas
# pré-definimos os valores de consumo de bebida por pessoa e o volume da garrafa
def calcular_bebidas(convidados, consumo_por_pessoa_ml =800, volume_garrafa_litro =2.25):
    total_ml = convidados * consumo_por_pessoa_ml # calcula o consumo de bebidas por convidado/ml
    total_litro= total_ml/1000 # converte o consumo para litro

    garrafas = int(total_litro/volume_garrafa_litro) # divide o total do consumo pelo volume da garrafa
    if total_litro % volume_garrafa_litro > 0: # se o resultado for um número decimal
        garrafas += 1 # acrescenta uma garrafa na compra
    return total_litro, garrafas # retorna o total em litros o o número de garrafas

resultado=calcular_bebidas(convidados)
print(resultado)

# resultado=calcular_bebidas(convidados)
# print(resultado)

def calcular_carne(convidados, consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama # informa a quantidade total  de carne em gramas
    total_kg= total_gramas/1000 # transformando o valor total em gramas para quilo
litros, garrafas = calcular_bebidas(convidados)
carne_kg= calcular_carne(convidados)
print('\n___quantidade total para churrasco___')
print(f"numero de convidados: {convidados}")
print(f'refrigerantes necessários:{litros:2.f} litros')
print(f"garrafas de 2.5L:{garrafas} unidades")
print(f"carne necessaria:{carne_kg:.2f} kg")