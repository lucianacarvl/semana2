# Questão 16
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a
# quantidades de latas de tinta a serem compradas e o preço total.
# 1L faz a cobertura de 3m².
# Sabendo que, se 1L cobre 3m², 18L cobrem 54m².

area_total = float(input("Informe a àrea total que vc deseja pintar em metros quadrados:"))
area_litro = 3
lata_litro = 18
valor_lata = 80
valor_total = (area_total * valor_lata) / (lata_litro * area_litro)
total_latas = area_total / (area_litro * lata_litro)

print("\n Para a área informada, o valor total é de R$ {:.2f}".format(valor_total))
print(f"\n O total de latas necessárias para pintar a área de {area_total:,.2f} m² é de {total_latas:,.2f} latas")