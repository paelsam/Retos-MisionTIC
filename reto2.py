# def nota_quices(codigo,n1,n2,n3,n4,n5):
#     lista_notas = [n1,n2,n3,n4,n5]
#     lista_notas2 = []
#     for nota in lista_notas:
#         nota_5 = (nota * 5) / 100
#         lista_notas2.append(nota_5)
#     nota_minima = min(lista_notas2)
#     lista_notas2.remove(nota_minima)
#     promedio = sum(lista_notas2) / 4
#     return f"El promedio ajustado del estudiante {codigo} es: {round(promedio, 2)}"
#     pass

def nota_quices(codigo,n1,n2,n3,n4,n5):
    nota_minima = min(n1,n2,n3,n4)
    promedio = ((n1 + n2 + n3 + n4 + n5 - nota_minima) / 4) * 5 / 100
    return f"El promedio ajustado del estudiante {codigo} es: {round(promedio, 2)}"

print(nota_quices("AA0010276",40,50,39,76,96))
print(nota_quices("AA0010895",88,66,44,22,41))
print(nota_quices("ACB044276",60,50,21,5,100))
print(nota_quices("ABO310276",100,93,88,99,96))
print(nota_quices("AT1055273",2,15,30,10,21))





