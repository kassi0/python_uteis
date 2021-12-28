#!/usr/bin/env python
"""
Criado em - 15/03/2021
Author - Cássio Telles
Versão 1.0

"""
import subprocess
import getpass
import os

opcao = 0

while opcao != 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('##################################################################################')
    print('#                                  FAKEJEC                                       #')
    print('#              SOFTWARE DE ACESSO REMOTO AOS COMPUTADORES TRE-BA                 #')
    print('#                  PRECISANDO DE SUPORTE LIGUE **************                    #')
    print('#                        E-MAIL: ***@*****************                           #')
    print('#                             www.tre-ba.jus.br                                  #')
    print('##################################################################################\n\n')
    print('SELECIONE A LOCALIZAÇÃO ONDE O SEU COMPUTADOR SE ENCONTRA!\n')
    print('''    [ 1 ] COMPUTADOR SECRETARIA
    [ 2 ] COMPUTADOR ZE CAPITAL
    [ 3 ] COMPUTADOR ZE INTERIOR
    [ 4 ] SAIR''')
    opcao = int(input('\n\nQual a Opção desejada? '))

    if opcao == 1:
        print('\nCOMPUTADOR SECRETARIA \n')
        print('EXEMPLO: "rbawSECRETARIA01"')
        computador = input('Digite o Nome do Computador: ')
        titulo = input('Título de Eleitor: ')
        pswd = getpass.getpass('Senha:')
        subprocess.call([f"rdesktop -u {titulo} -d *dominio.com* -p {pswd} -g 95% -a 24 -z -x lan -r sound:remote {computador}.*dominio.com*"],shell=True)

    elif opcao == 2:
        print('\nCOMPUTADOR ZE CAPITAL\n')
        print('EXEMPLO: "zbaZNEwks01"')
        computador = input('Digite o Nome do Computador: ')
        #titulo = input('Título de Eleitor: ')
        #pswd = getpass.getpass('Password:')
        processo = subprocess.call([f"rdesktop -d *dominio.com* -g 95% -a 24 -z -x lan -r sound:remote {computador}.*dominio.com*"],shell=True)

    elif opcao == 3:
        print('\nCOMPUTADOR ZE INTERIOR\n')
        print('Número referente a seu cartório: Exemplo - 192, 21, 205')
        ze = input('Digite o número da Zona Eleitoral: ')
        print('\nNúmero referente ao Computador utilizado: Exemplo - 1, 2, 3, 4, 5, 15')
        std = input('Digite o Número da STD: ')
        #titulo = input('Título de Eleitor: ')
        #pswd = getpass.getpass('Password:')
        processo = subprocess.call([f"rdesktop -g 95% -a 24 -z -x lan -r sound:remote 10.171.{ze}.{std}"],shell=True)

    elif opcao == 4:
        print('Finalizando...')

    else:
        print('Opção Inválida')

    print('Finalizado com Sucesso!')
