"""
Feito por Cássio Telles
"""
import subprocess
import os.path
import time

pathb = '/dev/sdb'
pathc = '/dev/sdc'
pathd = '/dev/sdd'
pathe = '/dev/sde'
isExistb = os.path.exists(pathb)
isExistc = os.path.exists(pathc)
isExistd = os.path.exists(pathd)
isExiste = os.path.exists(pathe)
while (True):
    os.system('cls' if os.name == 'nt' else 'clear')
    if isExistb is True:
        print('\nPenDrive conectado, Formatando /DEV/SDB!\n')
        subprocess.call(['mkfs.vfat -I -v -n "FORMATADO" /dev/sdb'], shell=True)
        print("\nPendrive /DEV/SDB Formatado indo para Próximo")
        time.sleep(5)
    if isExistc is True:
        print('\nPenDrive conectado, Formatando /DEV/SDC!\n')
        subprocess.call(['mkfs.vfat -I -v -n "FORMATADO" /dev/sdc'], shell=True)
        print("\nPendrive /DEV/SDC Formatado indo para Próximo")
        time.sleep(5)
    if isExistd is True:
        print('\nPenDrive conectado, Formatando /DEV/SDD!\n')
        subprocess.call(['mkfs.vfat -I -v -n "FORMATADO" /dev/sdd'], shell=True)
        print("\nPendrive /DEV/SDD Formatado indo para Próximo")
        time.sleep(5)
    if isExiste is True:
        print('\nPenDrive conectado, Formatando /DEV/SDE!\n')
        subprocess.call(['mkfs.vfat -I -v -n "FORMATADO" /dev/sde'], shell=True)
        print("\nPendrive /DEV/SDE Formatado Aguardando próxima Remessa")
        time.sleep(50)

    if isExistb is False:
        print('Não Encontrei algum dos PenDrives')
        time.sleep(20)

    elif isExistc is False:
        print('Não Encontrei algum dos PenDrives')
        time.sleep(20)

    elif isExistd is False:
        print('Não Encontrei algum dos PenDrives')
        time.sleep(20)

    elif isExiste is False:
        print('Não Encontrei algum dos PenDrives')
        time.sleep(20)

