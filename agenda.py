# AGENDA DE CONTATOS
# Desenvolva um programa que permita ao usuário adicionar, visualizar e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Dicionario contendo os contatos'''

contatos = [{'nome': 'Mãe'}]

def mensagem():
    print('''
=============== AGENDA VIRTUAL ================
            INFORME UMA DAS OPÇÕES ABAIXO:

[ 1 ] - ADICIONAR AOS CONTATOS  
[ 2 ] - VISUALIZAR LISTA DE COTATOS 
[ 3 ] - EDITAR CONTATOS
[ 0 ] - DESLOGAR                                                        
=================================================== ''')

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto.upper())
    print(linha)
    print() #Pular linha

def voltar_ao_menu():
    print() #Pular linha
    input('Digite uma tecla para voltar ao menu: ')
    main()

def opcao_invalida():
    print('Opção Invalída!!!')
    voltar_ao_menu()


def opcao_escolhida():
    os.system('cls')
    mensagem()
    try:
        opcao = int(input('Digite o número da opção: '))

        if opcao == 1:
            adicionando_contato()
        elif opcao == 2:
            lista_de_contatos()
            pass
        elif opcao == 3:
            editar_contato()
        elif opcao == 0:
            deslogando()
        else:
            pass
    except:
        opcao_invalida()   
            


def deslogando():
    exibir_subtitulo('Deslogado')

def lista_de_contatos():
    '''
Preciso zerar a lista de contato, está aparecendo um contato por padrão messmo antes do usuario adicionar
'''
    exibir_subtitulo('Lista de Contatos')

    print(f'Informações dos Contatos Salvos'.upper())
    for contato in contatos:
        nome_do_contato = contato['nome']
        print(f'Nome: {nome_do_contato} ')


    voltar_ao_menu()


def adicionando_contato():
    exibir_subtitulo('Adicionando Contato')
    print('Mínimo de 3 caracteres e Maximo de 18 caracteres')
    nome_do_contato = input('Nome do Contato: ')
    ''' 
    Validação de nome
    Preciso melhorar esse código
    '''
    while len(nome_do_contato) < 3 or len(nome_do_contato) > 18: #Enquanto o input receber menos 3 ou mais de 18 caracteres, a string não será armazenada        
        adicionando_contato()

    dados_do_contato = {'nome': nome_do_contato}
    contatos.append(dados_do_contato)
    print(f'\nO contato {nome_do_contato} foi salvo na agenda')

    voltar_ao_menu()

def editar_contato():
    '''Função responsavel por editar as informações do contato
    1- Editar o nome do contato
    '''
    exibir_subtitulo('Alterar informações dos contatos')
    for editar in contatos:
        print(editar)
        pass

    voltar_ao_menu()
def main():
    mensagem()
    opcao_escolhida()
    # exibir_subtitulo()

if __name__ == '__main__':
    main()