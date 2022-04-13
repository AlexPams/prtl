from secrets import choice

def generate(length, banned_symbols):
    symbols = ascii(banned_symbols)
    password = []
    for i in range(length):
        password.append(choice(symbols))
    return ''.join(password)


def ascii(banned_symbols):
    symbols = []
    for i in range(ord('!'), ord('~') + 1):
        if chr(i) in banned_symbols:
            continue
        symbols.append(chr(i))
    return symbols