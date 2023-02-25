from tpc2 import TPC2

def main():
    res = TPC2()
    c=-1  
    while c!=0:
        print("***** Somador on/off *****")
        print("  ")
        print("1 -> Programa que some todas as sequências de dígitos que encontre num texto")
        print("2 -> Programa que some todas as sequências de dígitos com a opção on, off e =")
        print("0 -> Sair")
        print("******************************")
        c = int(input("Indique a opção pretendida-> "))
        print (" ")
        if c==1:
            print("Insira o texto")
            userInput = input()
            print (" ")
            res.sumDigits(userInput)
            print (" ")
        if c==2:
            print("Insira o texto")
            userInput = input()
            print (" ")
            res.sumDigitsWithOptions(userInput)
            print (" ")

if __name__ == "__main__":
    main()