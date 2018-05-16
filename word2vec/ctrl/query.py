from django.http import HttpResponse

from word2vec.algo.trans import e2c, c2e
from word2vec.db.words import save_new_word
from word2vec.utils import json_helper


def query_save(query_lang, query_word, uid):
    if query_lang == 'zh':
        trans_result = e2c(query_word)
        save_new_word(query_word, trans_result, uid)
        return HttpResponse(json_helper.dumps_err(0, trans_result))
    else:
        trans_result = c2e(query_word)
        save_new_word(query_word, trans_result, uid)
        return HttpResponse(json_helper.dumps_err(0, trans_result))