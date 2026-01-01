"""
Write a function that takes an array of words and smashes them together
into a sentence and returns the sentence. You can ignore any need to
sanitize words or add punctuation, but you should add spaces between each word.
Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

"""


def join_words(words: list[str]) -> str:
    """Функция преобразует содержимое списка строк в одну строку, разделённую пробелами."""
    return " ".join(words)


if __name__ == "__main__":
    words = ['hello', 'world', 'this', 'is', 'great']
    print(join_words(words))