print("Doação de sangue")

idd = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso? "))
genero = input("Você é Homem ou Mulher(H/M)? ")
genero = genero.capitalize()
sangue = input("Você doou sangue nos ultimos 90 dias? (sim/nao) ")

if(genero == "M" or genero == "Mulher"):
    gravida = input("Você está grávida? (sim/nao) ")
    if(idd >= 16 and idd <= 69 and peso >= 50 and gravida == "nao" and sangue == "nao"): 
        print("Você pode doar sangue!")
if(idd >= 16 and idd <= 69 and peso >= 50 and sangue == "nao"): 
    print("Você pode doar sangue!")
else: 
    print("Você não pode doar sangue! ")
