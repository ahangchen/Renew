from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from word2vec.algo.trans import e2c, c2e
from word2vec.ctrl.query import query_save
from word2vec.ctrl.review import random_words
from word2vec.utils import json_helper


@csrf_exempt
def query(request):
    query_word = request.GET['word']
    query_lang = request.GET['lang']
    query_user = request.GET['usr']
    return query_save(query_lang, query_word, query_user)


@csrf_exempt
def review(request):
    return random_words()