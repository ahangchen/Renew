from random import sample

from word2vec.models import Word, Usr


def save_new_word(word, meaning, usr_id):
    Usr.objects.update_or_create(id=usr_id)
    Word.objects.update_or_create(word=word,  user_id=usr_id, defaults={'meaning': meaning, 'review_cnt': 0})


def review_words():
    all_word = Word.objects.all()
    cnt = all_word.count()
    word_ids = sample(range(1, cnt + 1), min(10, cnt))
    rand_words = all_word.filter(id__in=word_ids)
    for word in rand_words:
        word.review_cnt += 1
        word.save()
    return rand_words
