altura = float(input('Qual é sua altura em cm? '))
peso = float(input('Qual é o seu peso em Kg? '))

IMC = peso / (altura/100) **2

if IMC < 18.5:
  print('Magreza')
elif IMC >= 18.5 and IMC <= 24.9:
  print('Normal')
elif IMC >= 25.0 and IMC <= 29.9:
  print('Sobrepeso')
elif IMC >= 30.0 and IMC <= 39.9:
  print('Obesidade')
else:
  print('Obesidade grave')
        