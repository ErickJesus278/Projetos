print("Tabela Periódica")
print()
print("Elementos disponíveis: Na, H, Fe, C, Ti")

elemento = input("Digite o elemento: ")
elemento = elemento.capitalize()
n1 = 11
if(elemento == "Na"):
    print("Nome: Sódio")
    print("Massa do elemento: 22.99")
    print("Número: 11")
elif(elemento == "H"):
    print("Nome: Hidrogênio")
    print("Massa do elemento: 1.00784")
    print("Número: 11")
elif(elemento == "Fe"):
    print("Nome: Ferro")
    print("Massa do elemento: 55.845")
    print("Número: 26")
elif(elemento == "C"):
    print("Nome: Carbono")
    print("Massa do elemento: 12.011")
    print("Número: 6")
elif(elemento == "Ti"):
    print("Nome: Titânio")
    print("Massa do elemento: 47.867")
    print("Número: 22")
else:
    print("Erro, Verifique se o elemento está escrito corretamente e tente novamente!")
