import re
import sys
from itertools import product, cycle, izip, repeat, imap
from string import ascii_letters, punctuation, digits


def load_words():
    return frozenset(line.strip().lower() for line in open("/usr/share/dict/words") if len(line) > 3)


def read_cipher_text(file_name):
    with open(file_name) as f:
        cipher_text = [int(c) for c in f.read().split()]
    return cipher_text


def create_cipher_text(plain_text, password):
    plain_text = [ord(c) for c in plain_text]
    password = [ord(c) for c in password]
    cipher_text = []
    for (c, p) in izip(plain_text, cycle(password)):
        cipher_text.append(c ^ p)
    return cipher_text


def decipher(cipher_text, password, message_codes):
    plain_text = []
    for (c, p) in izip(cipher_text, cycle(password)):
        t = c ^ p
        if not (t in message_codes):
            return None
        plain_text.append(t)
    return plain_text


def try_password(args_tuple):
    password, data = args_tuple
    plain_text = decipher(data["cipher_text"], password, data["message_codes"])
    if plain_text is None:
        return None
    plain_text = "".join(chr(i) for i in plain_text)
    plain_words = {w.lower() for w in re.split(data["delimiters"], plain_text) if w.isalpha()}
    count = len(plain_words & data["words"])
    if count == 0:
        return None
    return count, "".join(chr(i) for i in password), plain_text


def brute_force(cipher_text, password_length, words, noise_cutoff):
    password_codes = [ord(c) for c in digits + ascii_letters]
    data = {"words": words, "cipher_text": cipher_text}
    data["message_codes"] = frozenset(range(32, 127) + [ord("\n")])
    data["delimiters"] = re.compile("|".join(map(re.escape, punctuation + " \n")))
    best_results, best_wc = [], 0
    for i in xrange(1, password_length + 1):
        for result in imap(try_password, izip(product(password_codes, repeat=i), repeat(data))):
            if result:
                if result[0] >= noise_cutoff:
                    print result[1], result[2]
                if result[0] > best_wc:
                    best_results, best_wc = [result], result[0]
                elif result[0] == best_wc:
                    best_results.append(result)
    print "\n\nBEST RESULTS:\n"
    for result in best_results:
        print result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        max_password_length, noise_cutoff, cipher_text = 3, 2, create_cipher_text("Hello, world!", "Az0")
    else:
        max_password_length, noise_cutoff, cipher_text = 20, 5, read_cipher_text(sys.argv[1])
    words = load_words()
    brute_force(cipher_text, max_password_length, words, noise_cutoff)
