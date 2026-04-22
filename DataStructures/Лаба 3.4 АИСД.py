import re
data = input("Введите текст: ")
bad_words = {r'пидор[асы]?\w*': "***", r'волкорез[асы]?\w*':"***", r'ублюдок[а]?\w*':"***", r'еблан[аы]?\w*':"***"}
def moderate(text):
    for pattern, replacement in bad_words.items():
        text = re.sub(pattern, replacement, text, flags=re.I)
    return text
print(moderate(data))