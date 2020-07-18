import json
from pprint import pprint


def load_file():
    with open('files/newsafr.json', encoding='utf-8') as file:
        news_data = json.load(file)
    return news_data


def words_in_news(news_data):
    words = dict()
    for item in news_data["rss"]["channel"]["items"]:
        words_in_line = item["description"].split()
        for word in words_in_line:
            if word in words:
                words[word] += 1
            else:
                if len(word) > 6:
                    words.update({word: 1})
    return words


def top_words(words):
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]


top = top_words(words_in_news(load_file()))
print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для .json файла')
for number, word in enumerate(top, 1):
    print(f'{number} - {word[0]}')
