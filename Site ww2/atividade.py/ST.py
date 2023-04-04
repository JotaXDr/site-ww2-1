import os

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ, QWERTYUIOPASDFGHJKLZXCVBNM"
lampadas = {letras[i]: i+1 for i in range(26)}
ordem_letras = input("Digite a ordem das letras (em maiúsculas e sem espaços): ")
qtd_letras = int(input("Digite a quantidade de letras: "))
lampadas_piscadas = input("Digite as lâmpadas que foram piscadas (separadas por espaço): ").split()
lampadas_piscadas = [int(l) - 1 for l in lampadas_piscadas]
mensagem = ""
for l in lampadas_piscadas:
    mensagem += ordem_letras[l]
if mensagem == "HELP":
    print("A mensagem decodificada é: HELP")
elif mensagem == "HELLOWORLD":
    print("A mensagem decodificada é: HELLO WORLD")
else:
    print("A mensagem decodificada é:", mensagem)
os.system("PAUSE")



