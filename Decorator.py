import datetime


def counter(func):
    def wrapper(*args):
        start = datetime.datetime.now()
        res = func(*args)
        finish = datetime.datetime.now() - start
        print(finish)
        return res
    return wrapper

@counter
def longest_words1(file):
    with open(file, encoding="utf-8") as text:
        cont = text.read().split()
        word_length = 0
        final_result = []
        for i in cont:
            if len(i) > word_length:
                word_length = len(i)
                final_result.clear()
                final_result.append(i)
            elif len(i) == word_length:
                final_result.append(i)
    return final_result

@counter
def longest_words2(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

file = "article.txt"
print('1', longest_words1(file))
print('2', longest_words2(file))


