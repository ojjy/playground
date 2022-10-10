
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal zero"
        print(f"An Instance CREATED: {name}")
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # method
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        # self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

item1 = Item("Phone", 100, 5)
# to access attributes
# item1.price = 100
# item1.quantity = 5

random_str = "aaa"
# random_str은 str객체로 str클래스의 member method에 접근하는 방법
print(random_str.upper())

item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())


# 문자열객체 1000이 3번 합쳐지는 연산 이 문제를 해결하기 위해 constructor에 파라미터에 type을 선언한다.
# item3 = Item("Laptop", "1000", 3)
# item3 = Item("Laptop", 1000, -3)
# class attribute
print(Item.pay_rate)
# instance attribute
print(item1.pay_rate)
print(item2.pay_rate)

# debug에 유용
print(Item.__dict__) #All the attributes for class level
print(item1.__dict__) #All the attributes for instance level


item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
# 0.7이 아니고 0.8이 된다.
print(item2.price)



item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# 5 instances
print(Item.all)

for instance in Item.all:
    print(instance.name)

