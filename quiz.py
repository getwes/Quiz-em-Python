print("seja muito bem vindo ao quiz do aprendiz de python")
answer_user = input("quer começar? (s/n)")
if answer_user != "s":
    quit()

score = 0

print("começando...")

print("quem desenvolveu o jogo grand theft auto (GTA)? \n (A) rockstar games \n (B) ubisoft \n (C) activision \n (D) EA \n")
answer_1 = input("resposta:")

if answer_1 == "A":
    print("correto!")
    score = score + 1

else:
    print("incorreto")

print("qual o nome do protagonista do jogo Gts  san andreas ? \n (A) carlos john \n (B) carl jonhson \n (C) carl jaqueline \n (D) carlos jonhson \n")
answer_2 = input("resposta:")

if answer_2 == "B":
    print("correto!")
    score = score + 1

else:
    print("incorreto")

print(f"quiz acabou.... pontuação: {score}/2")