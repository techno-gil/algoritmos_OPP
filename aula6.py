print('='*40)
print('*'*15,'FUNÇÕES','*'*15)
print('='*40)

def mensagem():
    print('Live 01 - Lsta, Dicionários e Funções')
    print('-'*40)
mensagem() 

###############################

def verificar_situacao(nota):
    if nota >= 5:
        print('Aprovado')
    else:
        print('Reprovado')
verificar_situacao(4.5)
print('-'*40)

################################

def calcular_media(nota1,nota2):  
    media = (nota1 + nota2) / 2
    return media 
media = calcular_media(9,8)
print(media)
print('-'*40)