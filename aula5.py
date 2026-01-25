print('='*40)
print('*'*9,'LISTAS + DICIONÁRIOS','*'*9)
print('='*40)

alunos = [
    {
        'Nome':'Ana',
        'Idade':22,
        'Notas':[
            4.0,
            6.7,
            9.0
        ]
    },

    {
        'Nome':'Pedro',
        'Idade': 44,
        'Notas': [
             7.0,
             9.0,
             9.5
        ]
     
     }
]

alunos[1]['Nome'] = 'Pedro da Silva'

print(alunos[1]['Notas'][2])
print('-'*40)

