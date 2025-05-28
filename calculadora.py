def calculadora():
    '''
    Calculadora de 4 operações

    Inputs:
    -números (x,y)
    -operação

    Output:
    -x 'operação' y
    '''
    try:
        x = int(input('Digite o primeiro número: '))
        op = input('Escolha a operação (+, -, *, /): ')
        y = int(input('Digite o segundo número: '))
        match op:
            case '+': print(f'Resultado: {x+y}')
            case '-': print(f'Resultado: {x-y}')
            case '*': print(f'Resultado: {x*y}')
            case '/': print(f'Resultado: {x/y}')
            case _: print('Operação inválida!')
    except ValueError:
        print('Erro: Entrada inválida! Digite apenas números.')
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida!')

calculadora()