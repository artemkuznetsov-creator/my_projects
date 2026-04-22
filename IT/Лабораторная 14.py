import matplotlib.pyplot as plt
import math
import numpy as np
import csv

mu = 7
sigma = 4
x_axis = np.linspace(0,20, 70)
def func(x, sigma, mu):
    y = (1/(sigma * math.sqrt(2 * math.pi))) * 2.17**(- ((x - mu)**2/sigma**2))
    return y
y = [func(x,sigma,mu) for x in x_axis]
y_error = [func(x+0.07, sigma, mu) for x in x_axis]

plt.plot(x_axis, y, label="обычные значния")
plt.plot(x_axis, y_error, label="ошибочные значния")
plt.grid()
plt.xlabel("ось икс")
plt.xlabel("ось игрек")
plt.title("функция")
plt.legend(title='обозначения')
plt.show()

plt.figure(figsize=(12,12))
y3 = np.random.randint(-1,1, 70)
def random_plot(x):
    plt.subplot(5, 2, x)
    plt.plot(x_axis, y3)
zadanie_3 = [random_plot(x) for x in range(1,11)]
plt.show()

data = [
    ["мероприятие", "время_в_часах"],
    ["Сон", 8],
    ["Работа/Учеба", 8],
    ["Прием пищи", 2],
    ["Дорога", 1.5],
    ["Спорт/Зарядка", 1],
    ["Личная гигиена", 1],
    ["Отдых/Развлечения", 2],
    ["Домашние дела", 1.5]
]
meropriyatiya = []
vremya = []
with open('14.4.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open('14.4.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        meropriyatiya.append(row[0])
        vremya.append(float(row[1]))
plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
plt.bar(meropriyatiya,vremya)
plt.title('Распорядок')
plt.xlabel('Мероприятия')
plt.ylabel('Время')
plt.xticks(rotation=45)
plt.grid()
plt.subplot(1,2,2)
plt.pie(vremya,labels=meropriyatiya)
plt.show()

normal = np.random.normal(size=200)
plt.figure(figsize=(7,4))
plt.subplot(1,2,1)
plt.hist(normal)
plt.savefig('hist.png')
plt.subplot(1,2,2)
plt.boxplot(normal)
plt.title("Работа с нормальнм распределением")
plt.show()

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
def linear_plot(x,y):
    return x**2 - 3*x*y + y**2 + 2*y + 5
plt.plot(x,y,linear_plot(x,y))




