class Item:
    # method
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item()
# to access attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

random_str = "aaa"
# random_str은 str객체로 str클래스의 member method에 접근하는 방법
print(random_str.upper())


item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))