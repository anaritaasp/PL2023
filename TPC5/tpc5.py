import re  
import sys

class TPC5():
    moedas = ["1c","2c","5c","10c","20c","50c","1e","2e"]

    def getSaldo(self,saldo):
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

    def print_saldo_format(self,saldo):
        coins = str(saldo).split(".")
        final_saldo = coins[0]+"e"+coins[1]+"c"
        return final_saldo


    def testNumero(self,telefone,saldoo):
        saldo = float(saldoo)
        if telefone.startswith("T="):
                telefone= telefone.replace("T=", "")
                if (telefone.isnumeric() == False):
                        print("ERRO: por favor introduza o número no formato correto (apenas dígitos)")
                        newTelefone = input()
                        self.testNumero(newTelefone,saldo)
                if (telefone.startswith('00')== False):
                        if (len(telefone)!= 9): 
                            print("ERRO: por favor insira 9 dígitos")
                            newTelefone = input()
                            self.testNumero(newTelefone,saldo)
                        if (telefone.startswith('601') or telefone.startswith('641')):
                            print ("Esse número não é permitido neste telefone. Queira discar novo número!")
                            newTelefone = input()
                            self.testNumero(newTelefone,saldo)
                        if (telefone.startswith('2')):
                            if (float(saldo) < 0.25): 
                                print ("Não tem saldo suficiente para efetuar esta chamada")
                            else: 
                                saldo -= 0.25
                                print ("saldo = ", self.print_saldo_format (saldo)) 
                        if (telefone.startswith('808')):
                            if (float(saldo) < 0.10): print ("Não tem saldo suficiente para efetuar esta chamada")
                            else: 
                                saldo -= 0.10
                                print ("saldo = ", self.print_saldo_format (saldo)) 
                        if (telefone.startswith('800')):
                            print ("saldo = ", self.print_saldo_format (saldo)) 
                elif (telefone.startswith('00')):
                        if (float(saldo) < 1.50): print ("Não tem saldo suficiente para efetuar esta chamada")
                        else: 
                                saldo -= 1.50
                                print ("saldo = ", self.print_saldo_format (saldo)) 
                    
                        

