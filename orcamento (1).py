# Calculadora de orçamento
# Escreva uma instrução de cada vez.
renda = float(input("Quanto é sua Renda :"))
 
#Despesas
despesa_1 = input("Quanto foi sua despesa ?")
numero_1 = float(despesa_1)

despesa_2 = input("Quanto foi sua  segunda despesa ?")
numero_2 = float(despesa_2)

despesa_3 = input("Quanto foi sua terceira despesa despesa ?")
numero_3 = float(despesa_3)

total_despesas = numero_1+ numero_2 + numero_3 #Calculo das Despesas
renda_pos_despesas =   renda - total_despesas

print(f"Renda: {renda:.2f}")
print(f"Despesas: {total_despesas:.2f}")
print(f"Saldo: {renda_pos_despesas:.2f}")