# AGENDA DE CONTATOS
# Desenvolva um programa que permita ao usuário adicionar, visualizar e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Lista contendo os contatos'''
lista_contatos = ['João','Vinicius','Michelle']

def limpa_terminal():
    os.system('cls')

def continuar(opcao):
    input('ENTER para continuar: ')            
    
def mensagem():
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
    limpa_terminal()
    nome_contato = input('Nome do contato: ').capitalize().strip()
    
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
        return executa_opcoes()       

def visualizar_lista():
    limpa_terminal()
    print('LISTA DE CONTATOS')
    '''Arrumei a exibição da lista de contatos, porém tenho que fazer um tratamento quando o usuario buscar o contato pelo número.'''
    for indice, i in enumerate(lista_contatos):
        print(f'{indice} - {i}')

def editar_lista():
    
    print('''
        5 - EDITAR
        6 - EXCLUIR
                    ''')
    opcao_editar = int(input('Número da opção desejada: ')) 

    if opcao_editar == 5:
        '''O -1 é para tratar o valor do usuario, já que para enumerar os contatos na lista acrescentei +1, aqui eu diminuo -1'''
        editar = int(input('Número do contato a editar: '))
        visualizar_lista()
        pass
    elif opcao_editar == 6:
        visualizar_lista()
        excluir = int(input('Número do contato a excluir: '))
        contato_excluido = lista_contatos.pop(excluir)
        print(f'O contato {contato_excluido} foi excluído!')        
        print(lista_contatos)
        continuar()



def executa_opcoes():
    limpa_terminal()
    mensagem()
    opcao = int(input('Digite o número da opção que deseja: '))
    if opcao == 1:
        adiciona_contato(opcao)
    elif opcao == 2:
        visualizar_lista()
    elif opcao == 3:
        editar_lista()

    return opcao
def main():
    limpa_terminal()
    mensagem()
    executa_opcoes()

if __name__ == '__main__':
    main()