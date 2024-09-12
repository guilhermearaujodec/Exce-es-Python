while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
        if a < 0 or b < 0:
            raise TypeError('O número deve ser positivo')                               # gera uma exceção
        c = a / b
        print(f'Resultado: {c}')
    except TypeError:
        print(f'ERRO: {msg}')
    except ValueError:
        print('ERRO: O valor informado deve ser inteiro.')
    except ZeroDivisionError:
        print('ERRO: Ocorreu uma divisão por zero.')
    except Exception as msg:                               # exceção genérica
        print(f'ERRO inesperado: {msg}')
    else:                                                  # executa se não tiver exceção
        print('Operação efetuada com sucesso.')
        break
    finally:                                               # é executado sempre
        print('Fim do programa.')

    print('Continua...')