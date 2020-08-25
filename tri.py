# Trie is a tree with words

# how to model this:

from typing import List
import logging

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self, log_level: str = logging.WARNING):
        self.root = TrieNode('')

        # this is how to log:
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger()

        # commonly a Node has a value

    def load(self, file_name: str):
        with open(file_name, 'r') as trie_words:
            for word in trie_words.readlines():
                word = word.strip()
                self.logger.info(f"adding word: {word}")
                self.add_word_to_trie(word, self.root)

    def add_word_to_trie(self, word: str, active_node: TrieNode):
        if not word:
            self.logger.info("Done Adding word!")

            active_node.is_word = True
            return
        first_letter = word[0]
        if word[0] in active_node.children:
            # move to next child node
            self.add_word_to_trie(word[1:], active_node.children[word[0]])
        else:

            self.logger.info(f"adding letter: {first_letter}")

            active_node.children[first_letter] = TrieNode(first_letter)
            self.add_word_to_trie(word[1:], active_node.children[first_letter])

    def search(self, prefix: str) -> List[str]:
        self.search_output = []
        active_node = self.root
        for letter in prefix:
            self.logger.info(f"looking at prefix letter:  {letter}")
            self.logger.info(f"Child values are:  {active_node.children.keys()}")
            if letter not in active_node.children:
                return self.search_output

            active_node = active_node.children[letter]
        # after prefix construct a word to return
        self._construct_search_output(prefix, active_node)
        return self.search_output

    def _construct_search_output(self, prefix: str, active_node: TrieNode) -> None:
        if active_node.is_word:

            self.search_output.append(prefix)
        for child_node in active_node.children.values():
            self._construct_search_output(prefix + child_node.value, child_node)
