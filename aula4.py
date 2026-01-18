print('='*40)

contador = 1 

nome_aluno = str(input('Nome: ')).title()
print('-'*40)

soma = 0 
while contador <= 4:
    nota = float(input(f'{contador}° Nota: '))
    soma += nota 
    contador += 1 
media = soma / 4

if media >= 5:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
print('-'*40)
print(f'Aluno: {nome_aluno}')
print(f'Média: {media}')
print(f'Situação: {situacao}')
print('-'*40)

