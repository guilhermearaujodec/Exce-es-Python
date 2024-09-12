def soma(a, b):
    # valida os tipos do parametros (obriga que sejam float)
    if type(a) != float or type(b) != float:
        raise TypeError('Os parametros da funcao devem ser float')
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('ERRO: Divisão por zero')


while True:
    try:
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')
        opcao = int(input('Opção: '))
    except ValueError:
        print('Erro. O valor deve ser inteiro')
    else:
        try:
            a = float(input('Primeiro numero: '))
            b = float(input('Segundo numero: '))
        except ValueError:
            print('ERRO. Os valores devem ser do tipo float')
        else:
            match opcao:
                case 1:
                    print(soma(a, b))
                case 2:
                    print(subtracao(a, b))
                case 3:
                    print(multiplicacao(a, b))
                case 4:
                    print(divisao(a, b))
                case 5:
                    break