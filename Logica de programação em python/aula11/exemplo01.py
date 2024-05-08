# Lista com dez espaços inicialmente vazios (repesentados por 0)
locais = [0,0,1,0,0,0,0,0,0,0]
# Define o número de tentativas
tentativas = 3
print("Bem-vindo ao jogo de caça ao tesoura!")
print("Tente encontrar o tesouro. Você tem 3 tentativas.")
print("Escolha um numero entre 0 e 9 para procurar o tesoura.")
# Inicializa o contador de tentativas
contador = 0
# Loop para as tentativas do usuário
while contador != tentativas:
    contador += 1
    palpite = int(input("Escolha um índice para procurar o tesouro: "))
    if 0 <= palpite <= 9: #Verificar se o palpite está dentro do intervalo
        if locais [palpite] == 1:
            print("Voce encontrou")
        else:
            print("Não é esse o local do tesouro. Tente novamente.")
    else:
        print("Por favor, insira um número entre 0 e 9.")
if(contador == tentativas):
    print(f"Suas tentativas acabaram! O tesouro estava no índice .")