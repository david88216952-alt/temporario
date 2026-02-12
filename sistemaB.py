def menu():
  while True:
    print("=====")
    print("1 - Consultar Saldo \n")
    print("2 - Realizar Depósito\n")
    print("3 - Consultar Saque\n")
    print("4 - Ver Histórico\n")
    print("5 - Sair\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao
   
 
 
 
 
 
 
 
# função consultar saldo
 
def consultar_saldo(saldo):
  return saldo
 
#saldo = 1000.00
#print(consultar_saldo(saldo))
 
# realizar deposito
 
def realizar_deposito(saldo, deposito):
  saldo += deposito
  return saldo
#deposito = float(input("Digite seu deposito: "))
#print(realizar_deposito(saldo, deposito))
 
# realizar saque
 
def realizar_saque(saldo, saque):
  saldo -= saque
  return saldo
#saque = float(input("Digite seu saque: "))
#print(realizar_saque(saldo, saque))
 
 
#==inicio=====================================================
 
print("BEM VINDO(A) AO NOSSO SISTEMA BANCÁRIO!\n")
 
saldo = 1000
