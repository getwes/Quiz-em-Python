print("seja muito bem vindo ao quiz do aprendiz de python")
answer_user = input("quer começar? (s/n)")
if answer_user != "s":
    quit()

print("começando...")

print("quem desenvolveu o jogo grand theft auto (GTA)? \n (A) rockstar games \n (B) ubisoft \n (C) activision \n (D) EA \n")
answer_1 = input("resposta:")

if answer_1 == "A":
    print("correto!")

else:
    print("incorreto")
