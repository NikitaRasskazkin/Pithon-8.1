from pprint import pprint
import time


# Чтение новостей из json файла. Возвращает генератор новостей.
def read_news_from_json_file():
    import json
    with open('files/newsafr.json', encoding='utf-8') as file:
        news_data = json.load(file)
    news_description_generator = (
        item["description"]
        for item in news_data["rss"]["channel"]["items"]
    )
    return news_description_generator


# Чтение новостей из xml файла. Возвращает генератор новостей.
def read_news_from_xml_file():
    import xml.etree.cElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("files/newsafr.xml", parser)
    root = tree.getroot()
    news_description_generator = (
        x.text
        for x in root.findall('channel/item/description')
    )
    return news_description_generator


# Обрабатывает список строк и возвращает топ 10 самых часто встречающихся слов длинна которых больше 6 символов
# в формате [слово, сколько раз встретилось].
def top_words(news_lines: iter):

    # Возвращает список слов (с повторениями) из переданного списка строк без знаков препинания
    # и приведённый к нижнему регистру.
    def split_lines(lines: iter):
        import string
        words_list = [
            word.strip(string.punctuation).lower()
            for line in lines
            for word in line.split()
        ]
        return words_list

    top_w = dict()
    words_in_lines = split_lines(news_lines)
    for word in words_in_lines:
        if len(word) > 6:
            top_w.update({word: words_in_lines.count(word)})
    return sorted(top_w.items(), key=lambda x: x[1], reverse=True)[:10]


# Выводит на экран полученый топ
def print_top_words(top: list):
    print()
    for number, word in enumerate(top, 1):
        print(f'{number}\t- {word[0]} ({word[1]})')
    print()


def main():
    json_top = top_words(read_news_from_json_file())
    start = time.time()
    xml_top = top_words(read_news_from_xml_file())
    print(time.time() - start)
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для .json файла')
    print_top_words(json_top)
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для .xml файла')
    print_top_words(xml_top)


main()
