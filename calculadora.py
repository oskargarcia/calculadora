num1 = int(input("\nIngrasa un numero==>  "))
operador = input("\nSelecciona (+),(-),(/),(*)==>  ")
num2 = int(input("\nIngrasa un numero==>  "))
while operador == "+":
    print(f"\nEl resultado de la suma es==>  {num1 + num2}")
    break
if operador == "-":
    print(f"\nEl resultado de la reta es==>  {num1 - num2}")
if operador == "/":
    print(f"\nEl resultado de la divicion es==>  {num1 / num2}")
if operador == "*":
    print(f"\nEl resultado de la multiplicacion es==>  {num1 * num2}")
else:
    print("\noperador no valido")