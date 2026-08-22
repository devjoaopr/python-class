def somarItens(*valores):
    print(f"recebi esses {valores}")
    return sum(valores)


print(somarItens(10, 20, 30))  # 1 valor
print(somarItens(10, 20))  # 2 valores
print(somarItens(1, 1, 1, 1, 1))  # 5 valores
