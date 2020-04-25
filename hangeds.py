# -*- coding: utf-8 -*-

import random

IMAGES = ['''

  +---+
  |   |
      |
      |
      |
      |
      =========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
      =========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
      =========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
      =========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
      =========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
      =========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
      =========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      =========''', '''
''']

WORDS = [
  'batman',
  'python',
  'javascript',
  'css',
  'java',
  '8cho',
  'programacion'
]

def random_word():
  idx = random.randint(0, len(WORDS) - 1)
  return WORDS[idx]


def display_board(hidden_word, tries):
  print(IMAGES[tries])
  print('\n')
  print(hidden_word)
  print(' --- * --- * --- * --- * --- * --- * --- * --- * ')


def run():
  word = random_word()
  hidden_word = ['-'] * len(word)
  tries = 0 

  while True:
    display_board(hidden_word, tries)
    current_letter = str(raw_input('Ingrese un caracter: '))

    letter_indexes = []
    for idx in range(len(word)):
      if word[idx] == current_letter:
        letter_indexes.append(idx)

    if len(letter_indexes) == 0 :
      tries += 1

    else: 
      for idx in  letter_indexes:
        hidden_word[idx] = current_letter

      letter_indexes = []

if __name__ == '__main__':
    print('B I E N V E N I D O   A  A H O R C A D O S ')
    run()
