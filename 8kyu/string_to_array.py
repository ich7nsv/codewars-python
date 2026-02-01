"""
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"""


def string_to_array(s: str) -> list:
    return s.split(" ")

if __name__ == "__main__":
    print(string_to_array(""))