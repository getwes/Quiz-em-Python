import random
 
print("sejam muito bem vindo ao guess number")
choice_number = input("digite o numero teto do desafio:")

if choice_number.isdigit():
   choicer_number = int(choice_number)
else:
    print("erro: valor informado não é numérico. favor  execute novamente e informe um numero!")
    quit()

random_number_number = random.radint(0, choice_number)

while true:
    answer_user = input("adivinhe o numero: ")