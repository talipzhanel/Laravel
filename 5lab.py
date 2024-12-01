import re

def find_words_with_same_letter_and_three_different_chars(text):
    return re.findall(r'\b(\w)\S{3}\1\b', text)

def is_only_latin_and_digits(text):
    return re.fullmatch(r'^[a-zA-Z0-9]+$', text) is not None

def replace_spaces_with_hyphen(text):
    return re.sub(r'\s+', '-', text)

def is_only_letters_and_one_space(text):
    return re.fullmatch(r'^[a-zA-Z]+( [a-zA-Z]+)*$', text) is not None

def is_valid_ipv4(ip):
    return re.fullmatch(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip) is not None

text = "aabb1234 a$bb a1a$1b a3b9b"
text_latin_digits = "abc123XYZ"
text_with_spaces = "Hello world here"
ip = "192.168.1.1"

print("1. Арасында 3 басқа символ бар екі бірдей әріптен тұратын сөздер:", find_words_with_same_letter_and_three_different_chars(text))
print("2. Жолдың тек латын әріптері мен цифрлардан тұратынын тексеру:", is_only_latin_and_digits(text_latin_digits))
print("3. Барлық бос орындарды сызықшаға ауыстыру:", replace_spaces_with_hyphen(text_with_spaces))
print("4. Жолда тек әріптер мен бір бос орыннан тұратын сөздер бар екенін тексеру:", is_only_letters_and_one_space(text_with_spaces))
print("5. Жолдың дұрыс IP-адрес (IPv4) екенін тексеру:", is_valid_ipv4(ip))
