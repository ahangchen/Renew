from random import randint
from django.http import HttpResponse

from word2vec.db.words import review_words
from word2vec.utils import json_helper


def random_words():
    queryset_words = review_words()
    resp_words = list()
    for review_word in queryset_words:
        resp_words.append(
            {
                'word': review_word.word,
                'meaning': review_word.meaning,
                'review_cnt': review_word.review_cnt
            }
        )
    return HttpResponse(json_helper.dumps_err(0, resp_words))