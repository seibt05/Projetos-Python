funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

list1 = set(tem_carro).intersection(turno_noite)
print(list1)

list2 = set(tem_carro).intersection(turno_dia)
print(list2)

list3 = set(funcionarios).difference(tem_carro)
print(list3)