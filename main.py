n0= 0
n1= 1
n2= 0
verifica_cpf1= 0
verifica_cpf2= 0
regiao = ["RS","DF-GO-MS-MT-TO","AC-AM-AP-PA-RO-RR","CE-MA-PI","AL-PB-PE-RN","BA-SE","MG","ES-RJ","SP","PR-SC"]
cpf = input("Digite um CPF:")
cpf_format= '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
for numeros in range (9):
    verifica_cpf1+= int(cpf[n0])*n1
    n0+= 1
    n1+= 1
verifica_cpf1 %=11
n0 = 0
for numeros in  range (10):
    verifica_cpf2+= int(cpf[n0])* n2
    n0+= 1
    n2+= 1
verifica_cpf2 %= 11
verifica_regiao= cpf[8]
if  verifica_cpf1== int(cpf[9]) and verifica_cpf2 == int(cpf[10]):
    print(f"Seu CPF é válido:{cpf_format}")
    print(f"A região do seu  cpf é {(regiao[int(verifica_regiao)])}")
else:
    print ("Seu CPF é inválido")

