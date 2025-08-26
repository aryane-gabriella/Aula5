"""3) Dadas as informações dos produtos de uma loja, crie uma lista dicionarizada para guardar os elementos fornecidos e em seguida crie uma função que receba a lista e a imprima.​

Dados:
produto: tv 50 polegadas - marca: Samsung,
produto: micro-ondas 10 litros – marca: Panasonic,
produto: Iphone 15 pro max - marca: Apple,
produto: smartphone redmi note 13 – marca: Xiaomi
Produto: lavadora 10 kg – marca: Brastemp
"""

def imprimir(produtos):

    print("****************** Produtos Cadastrados *************************")
    for prod in produtos:
        produto = prod["produto"]
        marca = prod["marca"]
        print(f"Produto : {produto} - Marca : {marca}")

produtos = [
    {"produto":"Tv 50 polegadas","marca":"Samsung"},
    {"produto":"Micro-ondas","marca":"Panasonic"},
    {"produto":"Iphone 15 pro max","marca":"Apple"},
    {"produto":"Smartphone redmi note 13","marca":"Xiaomi"},
    {"produto":"Lavadora 10 kg","marca":"Brastemp"}
]

imprimir(produtos)
