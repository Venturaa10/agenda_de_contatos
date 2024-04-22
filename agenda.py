# AGENDA DE CONTATOS
# Desenvolva um programa que permita ao usuário adicionar, visualizar e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Lista contendo os contatos'''
lista_contatos = ['João','Vinicius','Michelle']

def limpa_terminal():
    '''Função responsavél por limpar o terminal'''
    os.system('cls')

def continuar(opcao):    
    input('ENTER para continuar: ')            
    
def voltar():
    '''Função responsavél por retornar ao menu'''
    return escolhe_opcao()    

def mensagem():
    '''Função responsavél por exibir a mensagem com as opções possiveis na agenda'''
    print('''
=============== AGENDA VIRTUAL ================
            INFORME UMA DAS OPÇÕES ABAIXO:

[ 1 ] - ADICIONAR AOS CONTATOS  
[ 2 ] - VISUALIZAR LISTA DE COTATOS 
[ 3 ] - EDITAR CONTATOS
[ 0 ] - DESLOGAR                                                        
=================================================== ''')
    print() #Pula linha

def adiciona_contato(opcao):
    '''Função responsavél por adicionar um contato a agenda do usuario'''
    limpa_terminal()
    print('0 -> Para voltar ao menu!\n')
    nome_contato = input('Nome do contato: ').capitalize().strip()
    
    if nome_contato == '0':
        voltar()

    if len(nome_contato) < 0 or len(nome_contato) < 4:
        print('CONTATO NÃO ADICIONADO A LISTA\n')
        print('Deve conter no minimo 4 caracteres!')
        continuar(opcao)
        return 

    if nome_contato in lista_contatos:
        print(f'O contato {nome_contato} já existe na sua agenda\n')
        continuar(opcao)
        return adiciona_contato(opcao)

    else:
        lista_contatos.append(nome_contato)
        print(f'O Contato {nome_contato} foi adicionado(a) a sua agenda.\n')
        continuar(opcao)  
        return escolhe_opcao()       

def visualizar_lista(opcao):
    '''Função resposanvél por exibir a lista de contato'''
    limpa_terminal()
    print('LISTA DE CONTATOS')
    '''Arrumei a exibição da lista de contatos, porém tenho que fazer um tratamento quando o usuario buscar o contato pelo número.'''
    for indice, i in enumerate(lista_contatos):
        print(f'{indice} - {i}')

    # continuar(opcao)
    # return escolhe_opcao()

def editar_lista(opcao):
    '''Função responsavél por fazer alterações na lista de contatos, como editar ou excluir contato'''
    limpa_terminal()
    print('''
        5 - EDITAR
        6 - EXCLUIR
        0 - VOLTAR AO MENU
                    ''')
    try:
        opcao_editar = int(input('Número da opção desejada: ')) 
    except:
        input('\nOpção Invalída!')
        return editar_lista(opcao)
    
    if opcao_editar == 5:
        visualizar_lista(opcao)
        print() #Pula linha
        print('FAZER A LOGICA PARA EDITAR')
        print('0 -> Para voltar ao menu!\n')
        editar = int(input('\nNúmero do contato a editar: '))
        if editar == 0:
            return escolhe_opcao()
     
    elif opcao_editar == 6:
        visualizar_lista(opcao)
        excluir = int(input('Número do contato a excluir: '))
        contato_excluido = lista_contatos.pop(excluir)
        print(f'O contato {contato_excluido} foi excluído!')        
        print(lista_contatos)
        continuar(opcao)
        
    elif opcao_editar == 0:
        voltar()

    else:
        input('\nOpção Invalída!')
        return editar_lista(opcao)




def escolhe_opcao():
    '''Função responsavél pela execução da função que o usuario desejar fazer'''
    limpa_terminal()
    mensagem()
    try:
        opcao = int(input('Digite o número da opção que deseja: '))

    except:
        input('\nOpção Invalída!')
        return escolhe_opcao()
    
    if opcao == 1:
        adiciona_contato(opcao)
    elif opcao == 2:
        visualizar_lista(opcao)

    elif opcao == 3:
        editar_lista(opcao)

    elif opcao == 0:
        deslogar()
        
    else:
        input('\nOpção Invalída!')
        return escolhe_opcao()
        
    return opcao


def deslogar():
    '''Função responsavél por encerrar o programa'''
    limpa_terminal()
    print('DESLOGADO!')

def main():
    limpa_terminal()
    mensagem()
    escolhe_opcao()

if __name__ == '__main__':
    main()