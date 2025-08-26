"""3) Dadas as informações dos produtos de uma loja, crie uma lista dicionarizada para guardar os elementos fornecidos e em seguida crie uma função que receba a lista e a imprima.​

Dados:
produto: tv 50 polegadas - marca: Samsung,
produto: micro-ondas 10 litros – marca: Panasonic,
produto: Iphone 15 pro max - marca: Apple,
produto: smartphone redmi note 13 – marca: Xiaomi
Produto: lavadora 10 kg – marca: Brastemp
"""

produtos = [
    {"produto": "TV 50 polegadas", "marca": "Samsung"},
    {"produto": "Micro-ondas 10 litros", "marca": "Panasonic"},
    {"produto": "iPhone 15 Pro Max", "marca": "Apple"},
    {"produto": "Smartphone Redmi Note 13", "marca": "Xiaomi"},
    {"produto": "Lavadora 10kg", "marca": "Brastemp"}
]

def imprimir_produtos(lista):
    for item in lista:
        print(f"Produto: {item['produto']} - Marca: {item['marca']}")

imprimir_produtos(produtos)
