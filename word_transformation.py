from collections import defaultdict
from typing import List, Dict


def compare(wordsOnLeft, wordsOnRight):
    differencesCountInWord = 0
    for word in range(len(wordsOnLeft)):
        if wordsOnLeft[word] != wordsOnRight[word]:
            differencesCountInWord += 1
        if differencesCountInWord == 1:
            return True
        return False

def ladderLenght(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if not beginWord or endWord not in wordList:
        return 0

    level = 1
    wordQueue = []
    visited_words = set([])
    for word in wordList:
        if compare(word, beginWord):
            wordQueue.append(word,level)
            if word == endWord:
                return 2

    # once queue initialized:
    # pop things from beggining of the queue
    while wordQueue:
        currentWord, level = wordQueue.pop()
        level += 1
        visited_words.add(currentWord)
        for word in wordList:
            if word not in visited_words and compare(word, currentWord):
                wordQueue.append((word, level))
                if word == endWord:
                    return level

def preprocessor(start_word, end_word, word_list) -> Dict[str, str]:
    out_map = defaultdict(list)
    word_len = len(start_word)
    for words in range(word_len):

        intermidiate_string = f"{start_word[:words]}*{start_word[words + 1]}"
        out_map[intermidiate_string].append(start_word)
    for words in range(word_len):
        intermidiate_string = f"{end_word[:words]}*{end_word[words + 1]}"
        out_map[intermidiate_string].append(end_word)
    for word in word_list:
        for words in range(word_len):
            intermidiate_string = f"{word[:words]}*{word[words + 1]}"
            out_map[intermidiate_string].append(word)
    return out_map

myBeginWord = "hit",
myEndWord = "cog",
myWordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLenght(0, myBeginWord, myEndWord, myWordList))
