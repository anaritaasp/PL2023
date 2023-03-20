import re  
import sys

moedas = ["1c","2c","5c","10c","20c","50c","1e","2e"]

def getSaldo(saldo):
    final_saldo = 0
    for elem in saldo:
        if (elem.strip()== "1c"): final_saldo+=0.01
        elif (elem.strip()== "2c"): final_saldo+=0.02
        elif (elem.strip()== "5c"): final_saldo+=0.05
        elif (elem.strip()== "10c"): final_saldo+=0.10
        elif (elem.strip()== "20c"): final_saldo+=0.20
        elif (elem.strip()== "50c"): final_saldo+=0.50
        elif (elem.strip()== "1e"): final_saldo+=1.00
        elif (elem.strip()== "2e"): final_saldo+=2.00
    return final_saldo

def print_saldo_format(saldo):
    coins = str(saldo).split(".")
    final_saldo = coins[0]+"e"+coins[1]+"c"
    return final_saldo


def testNumero(numero,saldo):
    if (numero.isnumeric() == False):
        print("ERRO: por favor introduza o número no formato correto (apenas dígitos)")
    if (numero.startWwith('00')== False):
        if (len(numero)!= 9): print("ERRO: por favor insira 9 dígitos")
        if (numero.startWwith('601') or numero.startWwith('641')):
            print ("Esse número não é permitido neste telefone. Queira discar novo número!")
        if (numero.startWith('2')):
            if (saldo < 0.25): print ("Não tem saldo suficiente para efetuar esta chamada")
            else: saldo -= 0.25
        if (numero.startWith('808')):
            if (saldo < 0.10): print ("Não tem saldo suficiente para efetuar esta chamada")
            else: 
                saldo -= 0.10
                print ("saldo =", saldo)   
        else: #chamada 800, custo = 0
            print ("saldo =", saldo)
    elif (numero.startWwith('00')):
         if (saldo < 1.50): print ("Não tem saldo suficiente para efetuar esta chamada")
         else: 
                saldo -= 1.50
                print ("saldo =", saldo) 
            
                  

on = 0
line = input()
saldo = 0
if (re.fullmatch("LEVANTAR", line)):
    on = 1
    print ("Introduza Moedas.")
    usermoedas = input()
    if usermoedas.startswith("MOEDA"):
        usermoedas2= usermoedas.replace("MOEDA", "")
        user_moedas= usermoedas2.replace(".","")
        coins = re.split(",",user_moedas)
        valid_moedas=[]
        invalid_moedas=[]
        for coin in coins:
            if coin.strip() in moedas: valid_moedas.append(coin)
            else : invalid_moedas.append(coin)
        saldo = "%.2f" % getSaldo(valid_moedas)
        if len(invalid_moedas)>0: print (''.join(invalid_moedas)," - moeda inválida; saldo = ",print_saldo_format(saldo))
    telefone = input()
    if telefone.startswith("T="):
        telefone= telefone.replace("T=", "")
        if (telefone.isnumeric() == False):
                 print("ERRO: por favor introduza o número no formato correto (apenas dígitos)")
        if (telefone.startswith('00')== False):
                if (len(telefone)!= 9): print("ERRO: por favor insira 9 dígitos")
                if (telefone.startswith('601') or telefone.startswith('641')):
                    print ("Esse número não é permitido neste telefone. Queira discar novo número!")
                if (telefone.startswith('2')):
                    if (saldo < 0.25): print ("Não tem saldo suficiente para efetuar esta chamada")
                    else: saldo -= 0.25
                if (telefone.startswith('808')):
                    if (saldo < 0.10): print ("Não tem saldo suficiente para efetuar esta chamada")
                    else: 
                        saldo -= 0.10
                        print ("saldo = ", print_saldo_format (saldo)) 
                else: #chamada 800, custo = 0
                    print ("saldo = ", print_saldo_format (saldo)) 
        elif (telefone.startswith('00')):
                if (saldo < 1.50): print ("Não tem saldo suficiente para efetuar esta chamada")
                else: 
                        saldo -= 1.50
                        print ("saldo = ", print_saldo_format (saldo)) 
if (re.fullmatch("POUSAR", line)):
               on = 0
               print("troco =", print_saldo_format(saldo), "; Volte sempre!")
               
        