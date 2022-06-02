basket = list()
products = input("""Введите наименование товара (завершить - 'стоп'):
""").lower()
basket.append(products)
while products != "стоп":
    products = input("""Введите наименование товара (завершить - 'стоп'):
""").lower()
    basket.append(products)
print ("") 
print("--- Список товаров ---")
print ("") 
i = 0
while i < len(basket):
    print(basket[i])
    i += 1
    if basket[i] == "стоп":
        break

