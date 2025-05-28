import os

tarefas = []

def exibir_subtitulo(texto):
    '''
    Exibe o subtítulo da opção escolhida.
    '''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''
    Retorna ao menu principal, mostrando as opções disponíveis.
    '''
    input('\n"ENTER" para voltar ao menu principal')
    main()

def menu_principal():
    '''
    Exibe as opções disponíveis no gerenciador de tarefas.
    '''
    exibir_subtitulo('Gerenciador de Tarefas')
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas')
    print('3. Remover tarefa')
    print('4. Sair')

def finalizar():
    '''
    Encerra o programa.
    '''
    exibir_subtitulo('Saindo do gerenciador de tarefas. Até mais!')

def opcao_invalida():
    '''
    Apresenta mensagem de erro quando o usuário insere um opção inválida.
    '''
    print(f'Erro: Opção inválida! Escolha uma opção entre 1 e 4')
    voltar_ao_menu_principal()

def adicionar_tarefa():
    '''
    Recebe a tarefa digitada pelo usuário e adiciona na lista de tarefas.
    '''
    exibir_subtitulo('Adicionar Tarefa')
    tarefa = input('Digite a tarefa: ').strip()
    if tarefa:
        tarefas.append(tarefa)
        print('Tarefa adicionada!')
    else:
        print('Erro: A tarefa não pode estar vazia!')
    voltar_ao_menu_principal()

def visualizar_tarefas():
    '''
    Imprime a lista de tarefas adicionadas pelo usuário. 
    Caso a lista esteja vazia exibe um aviso.
    '''
    exibir_subtitulo('Visualizar Tarefas')
    if len(tarefas) > 0:
        for i,tarefa in enumerate(tarefas,1):
            print(f'{i}. {tarefa}')
    else:
        print('A lista de tarefas está vazia!')
    
    voltar_ao_menu_principal()

def remover_tarefa():
    '''
    Remove uma tarefa da lista.
    -Caso a lista esteja vazia exibe mensagem de erro.
    -Se o usuário digitar o nome da tarefa ou um número que não está na lista, exibe mensagem de erro.
    '''
    exibir_subtitulo('Remover Tarefa')
    if len(tarefas) > 0:
        try:
            remover = int(input('Digite o número da tarefa a ser removida: '))
            removida = tarefas.pop(remover-1)
            print(f'Tarefa "{removida}" removida!')
        except ValueError:
            print('Erro: Entrada inválida! Digite o número da tarefa.')
        except:
            print(f'Erro: Não existe tarefa {remover}! Digite um número válido')
    else:
        print('Erro: Nenhuma tarefa para remover!')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    '''
    Recebe do usuário o número da opção que será executada pelo gerenciador de tarefas.
    Se for digitado uma opção inválida, exibe mensagem de erro.
    '''
    try:
        opcao = int(input('Escolha uma opção: '))

        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                visualizar_tarefas()
            case 3:
                remover_tarefa()
            case 4:
                finalizar()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''
    Função principal do programa.
    '''
    os.system('cls')
    menu_principal()
    escolher_opcao()

if __name__ == '__main__':
    main()