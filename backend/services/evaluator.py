from __future__ import annotations

import math
import re
from typing import Dict


class ContentEvaluator:
    """Provides lightweight readability and coverage metrics."""

    def _syllable_count(self, word: str) -> int:
        vowels = "aeiouy"
        word = word.lower()
        count = 0
        prev_char_was_vowel = False
        for char in word:
            if char in vowels and not prev_char_was_vowel:
                count += 1
                prev_char_was_vowel = True
            else:
                prev_char_was_vowel = False
        if word.endswith("e") and count > 1:
            count -= 1
        return max(1, count)

    def flesch_reading_ease(self, text: str) -> float:
        sentences = max(1, len(re.findall(r"[.!?]", text)))
        words = re.findall(r"[a-zA-Z']+", text)
        word_count = len(words) or 1
        syllables = sum(self._syllable_count(word) for word in words)
        words_per_sentence = word_count / sentences
        syllables_per_word = syllables / word_count
        return round(206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word, 2)

    def evaluate(self, text: str) -> Dict[str, float | int]:
        words = re.findall(r"[a-zA-Z']+", text)
        unique_terms = len(set(word.lower() for word in words))
        readability = self.flesch_reading_ease(text)
        return {
            "word_count": len(words),
            "unique_terms": unique_terms,
            "flesch_score": readability,
        }

