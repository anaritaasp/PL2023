from tpc1 import TPC1

def main():
    res = TPC1()
    c=-1  
    while c!=0:
        print("***** RESOLUÇÃO DO TPC1 *****")
        print("  ")
        print("1 -> Calcula a distribuição da doença por sexo")
        print("2 -> Calcula a distribuição da doença por escalões etários")
        print("3 -> Calcula a distribuição da doença por níveis de colesterol.")
        print("4 -> Cria tabela de distribuição ")
        print("0 -> Sair")
        print("******************************")
        c = int(input("Indique a opção pretendida-> "))
        print (" ")
        arrayInfo = []
        if c==1:
            res.saveInfo(arrayInfo)
            res.distrDoencaPorSexo(arrayInfo)
            print (" ")
        if c==2:
            res.saveInfo(arrayInfo)
            res.distrEscalão(arrayInfo)
            print (" ")
        if c==3:
            res.saveInfo(arrayInfo)
            res.nivelColesterol(arrayInfo)
        if c==4:
            li=-1
            while li!=0:
                print("***** Selecione a distribuição para a tabela *****")
                print("  ")
                print("1 -> Distribuição da doença por sexo")
                print("2 -> Distribuição da doença por escalões etários")
                print("3 -> Distribuição da doença por níveis de colesterol.") 
                print("******************************")
                li = int(input("Indique a opção pretendida-> "))
                print (" ") 
                if li==1:
                    res.saveInfo(arrayInfo)
                    res.createTable(arrayInfo,1)
                if li==2:
                    res.saveInfo(arrayInfo)
                    res.createTable(arrayInfo,2)
                if li==3:
                    res.saveInfo(arrayInfo)
                    res.createTable(arrayInfo,3)

if __name__ == "__main__":
    main()