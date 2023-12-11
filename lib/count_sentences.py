#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._value = ""
    
    # Getters and setters of value string
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if not isinstance(value, str):
            print("Not of type string, insert string!")
        else:
            self._value = value

    value = property(get_value, set_value)

    # other instance methods
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        return len([s for s in self._value.split('.') if s.strip() != ''])

word = MyString()
word.value = "This is a string! It has three sentences. Right?"
print(word.count_sentences())