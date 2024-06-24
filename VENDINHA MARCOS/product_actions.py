from random import randint

def convert_id_to_product(id_list):
    
    res = int(input("Qual o ID do produto -> "))
    product = id_list[res]
    
    return product 

def remove_product_quantity(product_list, id_list):
    
    ques = input("Deseja remover por ID [1] ou pelo nome do produto [2] -> ")
    
    if ques == "1":
        pdct = convert_id_to_product(id_list)
        qnt = int(input("Quantidade a ser removida -> "))
        product_list[pdct] -= qnt
    
    elif ques == "2":
        pdct = input("Qual o nome do produto -> ")
        qnt = int(input("Quantidade a ser removida -> "))
        product_list[pdct] -= qnt
    
def add_product_quantity(product_list, id_list):
    
    ques = input("Deseja adicionar por ID [1] ou pelo nome do produto [2] -> ")
    
    if ques == "1":
        pdct = convert_id_to_product(id_list)
        qnt = int(input("Quantidade a ser adicionada -> "))
        product_list[pdct] += qnt
    
    elif ques == "2":
        pdct = input("Qual o nome do produto -> ")
        qnt = int(input("Quantidade a ser adicionada -> "))
        product_list[pdct] += qnt
    
def add_product(product_list, id_list):
    
    product = input("Insira o produto -> ")
    quantity = int(input("Insira a quantidade ->"))
    
    while True:
        new_id = str(randint(1, 999999))
        
        if new_id in id_list.keys():
            continue
        
        else:
            id_list[new_id] = product
            product_list[product] = quantity
            break