class WordsFinder:
    file_names = []
    def __init__(self,*files):
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = dict()
        for i in WordsFinder.file_names:
            with open(i, encoding='utf-8') as file:
                text = file.read().lower()
                text = text.replace('\n', ' ').replace('!', ' ').replace('?', ' ')
                text = text.replace('.', ' ').replace(',', ' ').replace('=', ' ')
                text = text.replace(':', ' ').replace(';', ' ').replace(' - ', ' ')
                text = text.split()
                all_words[i] = text
        return all_words

    def find(self,word):
        find_word = dict()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word.casefold():
                    find_word[name] = i+1
                    break
        return find_word

    def count(self,word):
        count_word = dict()
        for name, words in self.get_all_words().items():
            count = 0
            for i in range(len(words)):
                if words[i] == word.casefold():
                    count += 1
            count_word[name] = count
        return count_word





finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))