import random
import os
os.system("cls" if os.name == "nt" else "clear")
print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
import sys, time

verde		= "\033[33m"
azul		= "\033[34m"
amarelo		= "\033[32m"
vermelho	= "\033[31m"


def animation(texto):
    for msg in texto:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.10)


animation(f'''
{verde}coded by: ScottLuck

{vermelho}Github: {azul}github.com/yScottLuck{azul}

{amarelo}Carregando...
''')
time.sleep(10)
import os
os.system("cls" if os.name == "nt" else "clear")
print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
nome = str(input('Digite seu nome: '))
print(f'{vermelho}Olá {nome}, seja bem vindo ao meu jogo feito em python!!!')
time.sleep(2)
os.system("cls" if os.name == "nt" else "clear")
print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
print(f'''
[ 1 ] PEDRA

{azul}[ 2 ] PAPEL

{amarelo}[ 3 ] TESOURA
''')
esc = int(input(f'Escolha uma opção: {verde}'))
pc = random.randint(1, 3)
if esc == (1): #pedra
    if pc == (2):
        print('Sua escolha: Pedra')
        print('Pc: Papel')
        print('O computador ganhou.')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif pc == (1):
        print('Sua escolha: Pedra')
        print('Pc: Pedra')
        print('Empate.')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif pc (3):
        print('Sua escolha: Pedra')
        print('Pc: Tesoura')
        print('Você ganhou!!!')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
elif esc == (2): #Papel
    if pc == (1):
        print('Sua escolha: Papel')
        print('Pc: Pedra')
        print('Você ganhou!!!')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif pc == (2):
        print('Sua escolha: Papel')
        print('Pc: Papel')
        print('Empate.')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif pc == (3):
        print('Sua escolha: Papel')
        print('Pc: Tesoura')
        print('O computador ganhou.')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
elif esc == (3):
    if pc == (1):
        print('Sua escolha: Tesoura')
        print('Pc: Pedra')
        print('O computador ganhou')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif pc == (2):
        print('Sua escolha: Tesoura')
        print('Pc: Papel')
        print('Você ganhou!!!')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
    elif pc == (3):
        print('Sua escolha: Tesoura')
        print('Pc: Tesoura')
        print('Empate.')
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print('''
    _____       __                                      
   |_   _|     [  |  _                                  
     | |  .--.  | | / ] .---.  _ .--.  _ .--.    .--.   
 _   | |/ .'`\ \| '' < / /__\\[ `.-. |[ '/'`\ \/ .'`\ \ 
| |__' || \__. || |`\ \| \__., | | | | | \__/ || \__. | 
`.____.' '.__.'[__|  \_]'.__.'[___||__]| ;.__/  '.__.'  
                                      [__|              
''')
        print('Obggg por jogar meu joguinho humilde kkdkdksks')
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
#acabou porra
#vão se fude geral q tá vendo o raw
#(yScottLuck Gostoso porra)