# Tugas Praktikum Struktur Data - 0/1 Knapsack (OOP)
# 25 Mei 2023 Pukul 08.00 s.d 1 Juni 2023 Pukul 12.00 

import numpy as np
class knapsack:
    def __init__(self, calorie, price, stock, money):
        self.n = sum(stock)
        self.stock = stock
        self.money = money
        self.calorie = self.expand(calorie)
        self.price = self.expand(price)
        self.arr = np.zeros((self.n, money))

    def calculate(self, n = None, money = None): 
        if n == None or money is None:
            n = self.n - 1
            money = self.money - 1

        if self.arr[n][money] != 0:
            return self.arr[n][money]
        if n < 0:
            result = 0
        elif self.price[n] > money:
            result = self.calculate(n-1, money)
        else:
            val1 = self.calculate(n-1, money)
            val2 = self.calorie[n] + self.calculate(n-1, money - self.price[n])
            result = max(val1, val2)
        self.arr[n][money] = result
        return result

    def expand(self, item_list: list) -> list:
        expanded = []
        for i in range(len(item_list)):
            expanded += [item_list[i]] * self.stock[i]
        return expanded
        
def main():
    fruit = ["Apel", "Jeruk", "Pisang", "Kiwi", "Mangga"]
    calorie = [91, 71, 105, 103, 96]
    price = [2360, 2120, 1890, 3770, 2870]
    stock = [3, 3, 5, 10, 5]
    money = 25000
    kp = knapsack(calorie, price, stock, money)
    print(kp.calculate())

if __name__ == "__main__":
    main()