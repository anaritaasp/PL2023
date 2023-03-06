from alineaA import exA
from alineaB import exB
from alineaC import exC
from alineaD import exD

def main():
    res = exA()
    res1= exB()
    res2= exC()
    res3= exD()
    c=-1  
    while c!=0:
        print("***** Processador de Pessoas listadas nos Róis de Confessados *****")
        print("  ")
        print("1 -> Calcula a frequência de processos por ano (primeiro elemento da data")
        print("2 -> Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados")
        print("3 -> Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.")
        print("4 -> Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.")
        print("0 -> Sair")
        print("******************************")
        c = int(input("Indique a opção pretendida-> "))
        print (" ")
        if c==1:
            print(" Ano  :   Nr de Processos")
            listinha = res.parserTextFile()
            res.dictFrequency(listinha)
            print (" ")
        if c==2:
            proprios=[]
            apelidos=[]
            res1.parserNome(proprios,apelidos)
            print (" ")
            print("5 Nomes Próprios mais comuns:")
            print (" ")
            res1.NomeFrequency(proprios)
            print (" ")
            print("5 Apelidos mais comuns:")
            print (" ")
            res1.NomeFrequency(apelidos)
            print (" ")
        if c==3:
            listaaa = res2.parseRRR()
            res2.parentescoFrequency(listaaa)
        if c==4:
            res3.get20lines()
            res3.jsonFile()
            
            
  

if __name__ == "__main__":
    main()