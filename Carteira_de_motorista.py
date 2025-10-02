print("Carteira de motorista")

idd = int(input("Digite a sua idade: "))
em = input("Você passou pelo Exame Médico? (sim/nao) ")
vt = input("Você tem violações de trânsito registradas? (sim/nao) ")

if(idd >= 18 and em == "sim" and vt == "nao"): 
    print("Você pode ter sua carteira de motorista! ")
else: 
    print("Você não pode ter a sua carteira de motorista!")
