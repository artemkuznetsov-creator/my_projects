import re
data = input("Введите номер:")
result = re.findall(r'\+7[()0-9-]{1,}|\+380[()0-9-]{1,}',data)
print(result)