# TPC2: Somador on/off
class TPC2():

#um programa que some todas as sequências de dígitos que encontre num texto

    def sumDigits(self, userInput):
        result = [int(i) for i in userInput.split() if i.isdigit()]
        sum = 0
        for i in result:
            sum = sum + i
        print ("A soma total é", sum)


# Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado
# Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
# Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.
    def sumDigitsWithOptions(self, userInput):
        sum = 0
        flagOff= 0
        lista =[]
        result = userInput.split()
        for i in result:
                if (str(i) == "off" or str(i) == "Off" or str(i) == "OFF"): flagOff=1
                if (str(i) == "on" or str(i) == "ON"): flagOff=0
                if (str(i) == "="): break
                if flagOff == 0:
                     if i.isdigit(): lista.append(int(i))
        for i in lista:
                 sum = sum + i
        print ("A soma total é", sum)

            
                



        