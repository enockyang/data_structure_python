def index_words_new(text):
    if text:
        yield 0
    for index, letter in enumerate(text,1):
        if letter == ' ':
            yield index

for x in index_words_new('i am a good person'):
    print(x)