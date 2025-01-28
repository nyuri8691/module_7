from pprint import pprint
class Product:
    def __init__(self, name: str, weigth: float, category: str):
        self.name = name
        self.weigth = weigth
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weigth}, {self.category}')

class Shop(Product):
    __file_name = 'products.txt'
    def __init__(self, name = '', weight = 0.0, category = ''):
        Product.__init__(self, name = name, weigth = weight, category = category)
        Product.__str__(self)

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_ = file.read()
        file.close()
        return file_

    def add(self, *products):
        file = open(self.__file_name, 'a+')
        file.seek(0)
        f_list = file.readlines()
        file.close()
        flag = False
        for i in range(len(products)):
            products_str = products[i].__str__()
            for line in f_list:
                if products_str in line:
                    flag = True
            if flag:
                print(f'Продукт {products[i]} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{products[i]}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

#print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
