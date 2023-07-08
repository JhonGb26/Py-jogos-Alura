import forca
import alladivinhacao


def escolhe_jogo():  
    print("*" * 20)
    print("Escolha seu jogo!")
    print("*" * 20)

    print("(1) Forca (2) Adivinhação") 

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        alladivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()