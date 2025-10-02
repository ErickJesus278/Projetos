print("*Votação*")
print()

cand1_num   = 1
cand1_nome  = "João"
cand1_part  = "Partido A"
cand1_vice  = "Carol"

cand2_num   = 2
cand2_nome  = "Camila"
cand2_part  = "Partido B"
cand2_vice  = "Ângelo"

cand3_num   = 3
cand3_nome  = "Wellington"
cand3_part  = "Partido C"
cand3_vice  = "Lucas"

cand4_num   = 4
cand4_nome  = "Sabrina"
cand4_part  = "Partido D"
cand4_vice  = "Gislaine"

cand5_num   = 5
cand5_nome  = "Fábio"
cand5_part  = "Partido E"
cand5_vice  = "Vitoria"

cand6_num   = 6
cand6_nome  = "Daniel"
cand6_part  = "Partido F"
cand6_vice  = "Bianca"

cand7_num   = 7
cand7_nome  = "Thamires"
cand7_part  = "Partido G"
cand7_vice  = "Vitor"

cand8_num   = 8
cand8_nome  = "Yuri"
cand8_part  = "Partido H"
cand8_vice  = "Nicolas"

cand9_num   = 9
cand9_nome  = "Paulo"
cand9_part  = "Partido I"
cand9_vice  = "Thiago"

cand10_num  = 10
cand10_nome = "Ricardo"
cand10_part = "Partido J"
cand10_vice = "Kauan"

voto = int(input("Digite o seu voto de 1 a 10: "))

if(voto == 1):
    print("Voto: ", cand1_num)
    print("Candidato: ", cand1_nome)
    print(cand1_part)
    print("Vice: ", cand1_vice)
elif(voto == 2):
    print("Voto: ", cand2_num)
    print("Candidato: ", cand2_nome)
    print(cand2_part)
    print("Vice: ", cand2_vice)
elif(voto == 3):
    print("Voto: ", cand3_num)
    print("Candidato: ", cand3_nome)
    print(cand3_part)
    print("Vice: ", cand3_vice)
elif(voto == 4):
    print("Voto: ", cand4_num)
    print("Candidato: ", cand4_nome)
    print(cand4_part)
    print("Vice: ", cand4_vice)
elif(voto == 5):
    print("Voto: ", cand5_num)
    print("Candidato: ", cand5_nome)
    print(cand5_part)
    print("Vice: ", cand5_vice)
elif(voto == 6):
    print("Voto: ", cand6_num)
    print("Candidato: ", cand6_nome)
    print(cand6_part)
    print("Vice: ", cand6_vice)
elif(voto == 7):
    print("Voto: ", cand7_num)
    print("Candidato: ", cand7_nome)
    print(cand7_part)
    print("Vice: ", cand7_vice)
elif(voto == 8):
    print("Voto: ", cand8_num)
    print("Candidato: ", cand8_nome)
    print(cand8_part)
    print("Vice: ", cand8_vice)
elif(voto == 9):
    print("Voto: ", cand9_num)
    print("Candidato: ", cand9_nome)
    print(cand9_part)
    print("Vice: ", cand9_vice)
elif(voto == 10):
    print("Voto: ", cand10_num)
    print("Candidato: ", cand10_nome)
    print(cand10_part)
    print("Vice: ", cand10_vice)
else:
    print("Erro, Tente Novamente.")
