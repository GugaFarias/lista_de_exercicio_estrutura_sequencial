def calculo_area_circulo():

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

    print("Vamos calcular a area de um circulo")
raio = float(input("Digite o raio do circulo:"))

diametro = raio * raio

area_circulo = (3.141592 * diametro)

print("A area do círculo (π * 2)", area_circulo)