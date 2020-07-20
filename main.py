from pprint import pprint


# Чтение из файла данный. Возвращает прочитанные данные.
def load_file():
    import json
    with open('files/newsafr.json', encoding='utf-8') as file:
        news_data = json.load(file)
    return news_data


# Возвращает список топ 10 самых встречаемых слов длиннее 6 символов
# в формате: [слово, сколько раз встретилось слово].
def top_words(news_data):

    # Возвращает список слов (с повторениями) из переданой строки без знаков препинания.
    def split_line(line: str):
        import string
        words_list = line.split()
        for index, value in enumerate(words_list):
            words_list[index] = value.strip(string.punctuation)
        return words_list

    words = dict()
    for item in news_data["rss"]["channel"]["items"]:
        words_in_line = split_line(item["description"])
        for word in words_in_line:
            if word in words:
                words[word] += 1
            else:
                if len(word) > 6:
                    words.update({word: 1})
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]


def main():
    top = top_words(load_file())
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для .json файла')
    for number, word in enumerate(top, 1):
        print(f'{number} - {word[0]} ({word[1]})')


main()
