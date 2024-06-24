def get_products_from_product_database(products_path, products_list):
    
    with open(products_path, "r") as __db:
        _db = __db.read()
        db = _db.split("\n")
    
    for elements in db:
        
        if elements == "":
            continue
        
        info = elements.split("|")
        products_list[info[0]] = int(info[1])
    
def get_ids_from_ids_database(ids_path, ids_list):
    
    with open(ids_path, "r") as __db:
        _db = __db.read()
        db = _db.split("\n")
        
    for elements in db:
        
        if elements == "":
            continue
        
        info = elements.split("|")
        ids_list[info[0]] = info[1]

def save_products_in_product_database(products_path, products_list):
    
    with open(products_path, "w") as p_database:
        p_database.write("")
    
    for k, v in products_list.items():
        
        with open(products_path, "a") as p_database:
            add = k + "|" + str(v)
            p_database.write(f"{add}\n")
    
def save_ids_in_id_database(ids_path, ids_list):
    
    with open(ids_path, "w") as id_database:
        id_database.write("")
        
    with open(ids_path, "a") as id_database:
        
        for k, v in ids_list.items():
            add = k + "|" + v
            id_database.write(f"{add}\n")