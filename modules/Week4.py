import numpy as np
import matplotlib.pyplot as plt

filename = 'C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\befkbhalderstatkode.csv'

dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
       10: 'Amager Vest', 99: 'Udenfor'}


mask_2015 = (dd[:, 0] == 2015)


def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = dd[mask & (dd[:, 1] == n)]
    sum_of_people = all_people_in_given_n[:, 4].sum()  # index 4 is no of 'PERSONER'
    return sum_of_people


hood = np.array([number_of_people_per_neighbourhood(n, mask_2015) for n in neighb.keys()])

boroughs = list(neighb.values())
zipObj = zip(boroughs, hood)
answer = dict(zipObj)

sorted_answer = {}
sorted_keys = sorted(answer, key=answer.get)

for s in sorted_keys:
    sorted_answer[s] = answer[s]


def bars_neighb():
    inhabs = list(sorted_answer.values())
    plt.xlabel("Boroughs")
    plt.ylabel("Inhabitants")
    plt.title("Inhabs. per borough")
    plt.bar(boroughs, inhabs)
    plt.xticks(rotation=20, horizontalalignment='right', fontweight='light', fontsize='x-small')
    plt.show()


bars_neighb()


mask_over65 = (dd[:, 2] > 65)

print("Persons over 65:")
print(np.sum(dd[mask_2015 & mask_over65][:, 4]))

mask_nordic = (dd[:, 3] == 5104) | (dd[:, 3] == 5105) | (dd[:, 3] == 5106) | (dd[:, 3] == 5110) | (dd[:, 3] == 5120)

print("Persons from nordic countries ex. DK:")
print(np.sum(dd[mask_nordic & mask_2015 & mask_over65][:, 4]))



mask_osterbro = (dd[:, 1] == 2)
mask_vesterbro = (dd[:, 1] == 4)
years = list(range(1992, 2016))


def number_of_people_per_year(y, mask):
    all_people_in_given_y = dd[mask & (dd[:, 0] == y)]
    sum_of_people = all_people_in_given_y[:, 4].sum()
    return sum_of_people


sum_osterbro = np.array([number_of_people_per_year(y, mask_osterbro) for y in years])
sum_vesterbro = np.array([number_of_people_per_year(y, mask_vesterbro) for y in years])

def plot_neighb():
    plt.xlabel("År")
    plt.ylabel("Bydel")
    plt.title("Indbyggere pr. bydel")
    plt.plot(years, sum_osterbro, color='blue', label='Østerbro')
    plt.plot(years, sum_vesterbro, color='red', label='Vesterbro')
    plt.legend()
    plt.show()


#plot_neighb()