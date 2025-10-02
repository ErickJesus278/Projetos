print("*Senha*")
print()
si = False
while(si == False):
    s = input("Crie uma senha: ")
    if(len(s) < 8):
        si = False
        print("a senha precisa ter 8 caracteres.")
    elif(any(char.isdigit() for char in s)) and (any(char.isalpha() for char in s)):
        si = True
        print("Senha criada!")
    else:
        print("A senha precisa conter números e letras")
