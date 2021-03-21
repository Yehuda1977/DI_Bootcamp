import json

def retrieve_all_products():
    with open('products.json', 'r') as f:
        all_products = json.load(f)
    
    # print(type(all_products))
    # print("\nPrinting nested dicitonary as a key-value pair\n") 
    # for i in all_products: 
    #     print("ProductId:", i['ProductId']) 
    #     print("Category:", i['Category']) 
    #     print("MainCategory:", i['MainCategory']) 
    #     print() 
    return all_products

def retrieve_requested_product(id, all_products):
    for i in all_products:
        if i['ProductId'] == id:
            print(i)
            return i

# print(retrieve_all_products())
# all_products = retrieve_all_products()

# print(retrieve_requested_product('HT-1001', all_products))
    