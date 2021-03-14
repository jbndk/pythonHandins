import wget as wget

name_list = ["Viktor", "Sonya", "Jack"]


class IterNames:

    def __iter__(self):
            return self

    def __next__(self):
        print("Hi!")
        return 1


iterable = IterNames()
my_iter = iter(iterable)
print(next(my_iter))

#name_list = wget -O unisex_navne.xls https://ast.dk/_namesdb/export/names?format=xls&gendermask=4