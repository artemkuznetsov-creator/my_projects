seconds = int(input('Введите целое количество секунд:'))
days = 0
hours = 0
minutes = 0
if seconds >= 86400:
    days = seconds//86400
    seconds -= days*86400
if seconds >=  3600:
    hours = seconds // 3600
    seconds -= hours*3600
if seconds >= 60:
    minutes = seconds // 60
    seconds -= minutes * 60
print(f'{days} дней {hours} часов {minutes} минут {seconds} секунд')