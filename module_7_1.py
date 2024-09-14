from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        tovar = f'{self.name}, {self.weight}, {self.category}'
        return str(tovar)


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        doc = file.read()
        file.close()
        return doc

    def add(self, *products):
        list1 = open(self.__file_name, "a")
        for pos in products:
            if str(pos) not in Shop.get_products(self):
                list1.write(str(pos) + '\n')
            else:
                print(f'Продукт {str(pos)} уже есть в магазине')
        list1.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
