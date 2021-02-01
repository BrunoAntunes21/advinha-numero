import random as rd

numSorte=rd.randint(1,20)

def palpite(y,opc):

      if opc==0:
            print("encerrando")
            return False
      elif(opc==y):
            print("acertou")
            resp=input("deseja reiniciar?")
            if resp.lower()=='sim'or resp.lower()=="s"or resp.lower()=="yes"or resp.lower()=="y":
                return True
            elif resp.lower()=='não'or resp.lower()=="n"or resp.lower()=="no"or resp.lower()=="n":
                return False
            else:
                print("erro abortando o processo...")
                return False
      elif(opc<y):
          print("errou valor muito baixo")
          return True
      elif(opc>y):
          print("errou valor muito alto")
          return True







jogar=True
while jogar==True :
    try:
        x=int(input("insira o valor de 1  a 20(0 para encerrar)"))
        jogar=palpite(numSorte,x)

    except ValueError:
        print("insira apenas valores inteiros ou digite 0 para encerrar")
        jogar=True
