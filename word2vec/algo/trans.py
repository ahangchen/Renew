from googletrans import Translator

from word2vec.db.words import save_new_word


def e2c(en_word):
    translate = Translator()
    result = translate.translate(en_word, dest='zh-CN')
    return result.text
    # return 'ceshi'


def c2e(ch_word):
    translate = Translator()
    result = translate.translate(ch_word, dest='en')
    return result.text
    # return 'test'