import sys
from itertools import cycle, izip
from collections import Counter


def load_words():
    return frozenset(line.strip().lower() for line in open("/usr/share/dict/words") if len(line) > 3)


def read_cipher_text(file_name):
    with open(file_name) as f:
        cipher_text = [int(c) for c in f.read().split()]
    return cipher_text


def most_frequent_symbol(stripe):
    return Counter(stripe).most_common(1)[0][0]


def make_password(password_length, cipher_text):
    # split the text into stripes of password_length and find the most common
    # symbol, presumably, a space (32 in ASCII)
    guessed_spaces = (most_frequent_symbol(stripe) for stripe in
                      (cipher_text[i::password_length] for i in xrange(password_length)))
    return [i ^ 32 for i in guessed_spaces]


def decipher(cipher_text, password, message_codes):
    plain_text = []
    for (c, p) in izip(cipher_text, cycle(password)):
        t = c ^ p
        if not (t in message_codes):
            return None
        plain_text.append(t)
    return plain_text


def decrypt(cipher_text, words, max_password_length):
    message_codes = frozenset(range(32, 127) + [ord("\n")])
    for l in xrange(max_password_length):
        raw_password = make_password(l, cipher_text)
        password = "".join(chr(i) for i in raw_password)
        if password.lower() in words:
            raw_plain_text = decipher(cipher_text, raw_password, message_codes)
            if raw_plain_text is None:
                continue
            print "".join(chr(i) for i in raw_plain_text)
            print "\nThe password is {0}\n\n".format(password)
            reply = raw_input("Continue? (y/n) ")
            if reply.lower().startswith("n"):
                break


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Need a cipher text to decrypt."
    else:
        decrypt(read_cipher_text(sys.argv[1]), load_words(), 20)
