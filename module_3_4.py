def single_root_words(root_word, *other_words):
    # создадим пустой список
    same_words = list()
    list_words = list(other_words)
    # занижение регистра
    lower_list = [s.lower() for s in list_words]
    root_word_lower = root_word.lower()
    # перебор подходящих слов
    for i in range(len(lower_list)):
        # которые содержат root_word или наоборот root_word содержит одно из этих слов
        if (root_word_lower in lower_list[i]) or (lower_list[i] in root_word_lower):
            same_words.append(list_words[i])
    # возврат образованного спиcка
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
