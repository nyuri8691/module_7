import pprint

word = 'teXT'


class WordsFinder:

    res = {}

    def __init__(self, *file_names):
        self.file_names = list(file_names)

      #  self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = ',.=!?;:'

        for filename in self.file_names:
            words = []
            clear_line = ''
            with open(filename, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    while line.find(' — ') != -1:
                        line = line.replace(' — ', " ")
                        continue
                    for char in line:  # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':'] в строке.
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()
            all_words[filename] = words
            self.res.clear()
        return all_words

    def find(self, word):

        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower()) + 1
                self.res[names] = place
        return self.res

    def count(self, word):
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find(word), f' # Позиция первого искомого слова "{word}" в списке:', *finder1.res.values())
print(finder1.count(word), f' # Количество повторений найденного слова "{word}": ', *finder1.res.values(), '\n')

#finder2 = WordsFinder('Mother Goose - Monday’s Child.txt', )
#print(finder2.get_all_words())
#print(finder2.find('Child'))
#print(finder2.count('Child'), '\n')

#finder3 = WordsFinder('Rudyard Kipling - If.txt',)
#print(finder3.get_all_words())
#print(finder3.find('if'))
#print(finder3.count('if'), '\n')

#finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
#print(finder4.get_all_words())
#print(finder4.find('captain'))
#print(finder4.count('captain'), '\n')

#finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                     'Rudyard Kipling - If.txt',
#                    'Mother Goose - Monday’s Child.txt')
#pprint.pprint(finder1.get_all_words())
#print(finder1.find('the'))
#print(finder1.count('the'))
