import random


class Pizzeria:
    def invite(self):
        print('Все дороги ведут в Pizzeria!')


class Chef(Pizzeria):

    def __init__(self):
        self.mood = 50
        self.energy = 8
        self.money = 0

    def bake(self, customer_order):
        if self.energy >= customer_order:
            efficiency = 'Хорошо потудился, но устал'
            self.mood += 10
            self.money += 450
        else:
            efficiency = 'Медленно работал'
            self.mood -= 10
        return efficiency

    def earn(self):
        print('Повар получил зарплату', self.money)


class Customer(Pizzeria):

    def __init__(self):
        self.money = 3000
        self.mood = 70

    def make_order(self):
        order = random.randrange(1, 12)
        print('Хочу заказать ', order, ' пицц')
        return order

    def get_satisfaction(self):
        self.mood += 20
        print('Спасибо. Очень вкусно')

    def be_angry(self):
        self.mood -= 20
        print('Худшая пиццерия в городе!')


class Owner(Pizzeria):

    def __init__(self):
        self.money = 10000
        self.mood = 70

    def buy(self):
        print('Закупаю продукты')
        products = random.randrange(7)
        self.money -= 1000
        return products

    def get_profit(self):
        self.money += 3000
        print('Моя пицца понравилась покупателю!')

    def be_angry(self):
        self.money -= 1000
        print('Scusi. Оштрафую повара!')

    def pay_wages(self):
        self.money -= 650

    def earn(self):
        print('Состояние владельца', self.money)


class Caterer(Pizzeria):

    def __init__(self):
        self.money = 0
        self.goods = 4

    def supply(self, products_delivery):
        if self.goods >= products_delivery:
            supply_condition = 'Поставка продуктов осуществлена'
            self.money += 1000
            self.goods -= products_delivery
        else:
            supply_condition = 'Поставка продуктов не осуществлена'
        return supply_condition

    def earn(self):
        print('Поставщик получил', self.money)


class Cleaners(Pizzeria):

    def __init__(self):
        self.money = 0
        self.mood = 0

    def get_work(self):
        self.money += 200
        self.mood += 100
        print('Уборщица: Ура! Есть работа.')

    def earn(self):
        print('Уборщица заработала', self.money)


cooker = Chef()
buyer = Customer()
boss = Owner()
provider = Caterer()
cleaner = Cleaners()


products_delivery = boss.buy()
supply_satisfaction = provider.supply(products_delivery)
if supply_satisfaction == 'Поставка продуктов осуществлена':
    print('Пиццерия открыта!')
    customer_order = buyer.make_order()
    cooker_satisfaction = cooker.bake(customer_order)
    if cooker_satisfaction == 'Хорошо потудился, но устал':
        cooker.energy -= 3
        buyer.get_satisfaction()
        if buyer.mood > 89:
            boss.get_profit()
            print('Viva Italia!')
    else:
        buyer.be_angry()
        if buyer.mood < 51:
            boss.be_angry()
            cooker.money -= 300
    cleaner.get_work()
    boss.pay_wages()
else:
    print('Пиццерия закрыта по техническим причинам!')

pizzeria = [cooker, boss, provider, cleaner]
for worker in pizzeria:
    worker.earn()
if cooker.energy < 8:
    print('Повару нужно отдохнуть, его работоспособность: ', cooker.energy)
for person in pizzeria:
    person.invite()
