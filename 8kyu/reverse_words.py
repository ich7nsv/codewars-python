"""
Complete the function that accepts a string parameter,
and reverses each word in the string.

All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text: str) -> str:
    """Функция переворачивает каждое слово, сохраняя пробелы"""
    words = text.split(" ")
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return ' '.join(reversed_words)


if __name__ == "__main__":
    print(reverse_words("This is an example!"))