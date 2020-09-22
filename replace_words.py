from typing import List
from typing import Set


def process_word(word: str, word_set: Set[str]) -> str:
    for i in range(1, len(word)):
        if word[:i] in word_set:
            return word[:i]
    return word


def replace(self, words: List[str], sentence: str) -> str:
    word_set = set(words)
    sentence_parsed = sentence.split()
    for i, word in enumerate(sentence_parsed):
        sentence_parsed[i] = process_word(word, word_set)

    return " ".join(sentence_parsed)


word_list = ["aa", "app", "sam"]
sentence = "aaron ate the apple same way"
print(replace(0, word_list, sentence))
