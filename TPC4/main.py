from tpc4 import TPC4

def main():
    res = TPC4()
    c=-1  
    print("*****  Ficheiros CSV com listas e funções de agregação *****")
    print("  ")
    csvPath = str(input("Introduza o path do ficheiro CSV-> "))
    jsonPath = str(input("Introduza o path do ficheiro JSON-> "))
    #res.convertCVStoJSON(csvPath,jsonPath)
    res.make_json(csvPath,jsonPath)
        

  

if __name__ == "__main__":
    main()