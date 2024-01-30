# Nesse exemplo, usa-se o FINALLY para uma segunda chance de rodar o programa com correção da exceção apresentada.

nome = 'AndrePerez' 
idade = 19

try:
    apresentacao= 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
    print(apresentacao)
except TypeError: idade = str(idade)

finally:
    print('Segunda chance') 
    apresentacao= 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
    print(apresentacao)