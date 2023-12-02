#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=[], last_transaction=0):
      self.discount = discount
      self.total = total
      self.items = items
      self.items = []
      self.last_transaction = last_transaction

    def add_item(self, item, price, amount=1):
          self.total += (price * amount)
          self.last_transaction = price * amount
          for n in range(amount):
              self.items.append(item)  

    def apply_discount(self):
       if self.discount == 0:
           print("There is no discount to apply.")
       else:
           self.total -= (self.discount/100) * self.total
           print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        (self.items).pop()
        if self.items == []:
            self.total = 0
        else:
            self.total -= self.last_transaction
            print (self.items)