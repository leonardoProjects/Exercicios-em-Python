"""
DESAFIO 042: Analisando Triângulos v2.0
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

r1 = float(input('Primeiro segmento: ')) 
r2 = float(input('Segundo segmento: ')) 
r3 = float(input('Terceiro segmento: ')) 

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')

if r1 == r2 == r3:
    print('Equilátero')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('Isósceles')
elif r1 != r2 != r3:
    print('Escaleno') 