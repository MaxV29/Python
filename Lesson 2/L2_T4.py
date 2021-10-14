words = input("Введите текст: ").split()

for count, word in enumerate(words):
    print(f'{count}. {word[:10]}')