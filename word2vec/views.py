# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from word2vec.ctrl.query import query_save
from word2vec.ctrl.review import random_words


@csrf_exempt
def query(request):
    query_word = request.GET['word']
    query_lang = request.GET['lang']
    query_user = request.GET['usr']
    return query_save(query_lang, query_word, query_user)


@csrf_exempt
def review(request):
    return random_words()