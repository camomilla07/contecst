import datetime


class MyTime:
    def __init__(self, path):
        self.path = path
        global dt
        dt = datetime.datetime.now()
        print(f'Время запуска кода {dt}')

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        now = datetime.datetime.now()
        print(f'Время окончания работы кода {now}')
        print(f'{now - dt} потрачено на выполение кода')


if __name__ == '__main__':
    with MyTime('testfile.txt') as f:
        cook_book = {}
        for line_d in f:
            name_dish = line_d.strip()  # 1 строчка
            amount = f.readline().strip()  # 2 строчка
            ingredients = []
            x = int(amount)
            for line in range(x):
                ingredient = f.readline().strip().split('|')  # 3 строчка
                ingredient_d = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                ingredients.append(ingredient_d)
                a = {name_dish: ingredients}
                cook_book.update(a)
            f.readline().strip()  # пустая строчка
        print(cook_book)
