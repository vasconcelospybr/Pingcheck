import os, winsound, sys, time, datetime
from datetime import datetime, date, time, timezone


file = open("IPs.txt","r+")

with open("IPs.txt","r") as file:

  for line in file:
     response =  os.system("ping "  + line)

     if response == 0:
        print("")
        print("NOBREAK UP")
        print("")
        
        os.system("cls")

     else:
        
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 250  # Set Duration To 500 ms == 0.25 second
        winsound.Beep(frequency, duration)

        data_atual = date.today()
        data_atual = data_atual.strftime("%d%m%Y")

        hora_atual = datetime.now()
        hora_atual = hora_atual.strftime("%H%M%S")
        
        
        arquivo = open('IPsCheck.txt', 'r') # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        conteudo.append(line)   # insira seu conteúdo
        arquivo = open('IPsCheck.txt', 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
               
        arquivo.close()

        print("")
        print("NOBREAK DOWN")
        print("")
               
        os.system("cls")
print("")
print ("╔════════════════╗")
print ("|██████████ 100% = Concluído")
print ("╚════════════════╝")


os.system("IPsCheck.txt") #abre arquivo.txt na tela
sys.exit()