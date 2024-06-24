#Marcos é dono de uma franquia das lojas americas, por diversas dificudades no gerenciamento de seu armazem ele
# precisa de um sistema que registre produtos comprados para a loja e a quantidade restantes de cada produto, o
# sistema também tem que dar um id para cada produto e registrar esses dados em em uma dataBase, ele também precisa
# que o sistema avise quando faltar menos de 3 exemplares de algum produto.
#instruções:
#-Crie uma data base em txt para os produtos e dados do armazem de Marcos.
#-Faça um sistema que acesse a data base e que consiga tratar os dados retornados, o sistema também deve conseguir
# adicionar produtos no banco de dados e acessa-los pelo nome do produto ou pelo seu Id
#-o sistema deve ter uma "interface" de terminal que dê acesso a marco a acessar e adicionar seus produtos,
# deleta-los, ver a quantidade de cada um e que avise a ele quando faltar menos de 3 exemplares de algum produto

from data_treatment import *
from product_actions import *

products = {}
ids = {}

get_ids_from_ids_database("./lista_de_ids.txt", ids)
get_products_from_product_database("./produtos.txt", products)

while True:

    print(products)
    
    res = input("Qual ação deseja fazer, Marcos?\n[1] Adicionar produto\n[2] Adicionar certa quantidade de produto\n[3] Remover certa quantidade do produto\n[4] Fechar programa")

    if res == "1":
        add_product(products, ids)
        
    elif res == "2":
        add_product_quantity(products, ids)
        
    elif res == "3":
        remove_product_quantity(products, ids)
        
    elif res == "4":
        save_ids_in_id_database("./lista_de_ids.txt", ids)
        save_products_in_product_database("./produtos.txt", products)
        exit()
        