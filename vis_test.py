import pytest

import vis

word = 'text'
x_word = '_ _ _ _'
msg = 't'
x_word_new = 't _ _ t'

def test_secret_word():
	secret_word = vis.secret_word(word)
	assert secret_word == x_word

def test_open_secret_word():
	open_secret_word = vis.open_secret_word(msg, word)
	assert open_secret_word == x_word_new

def test_merger():
	merger = vis.merger(x_word, x_word_new)
	assert merger == x_word_new