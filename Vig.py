def alphabet(version=0) -> list:
    """
    Return Russian Alphabet
    :param version: just or random abc
    :return: List
    """
    # Creating classic alphabet
    if version == 0:
        l_abc = "".join([chr(i) for i in range(1040, 1072)])
        l_abc = l_abc[0:6] + "Ё" + l_abc[6:]
    # Creating random alphabet
    else:
        import random
        alpha = [chr(i) for i in range(1040, 1072)]
        alpha.append("Ё")
        l_abc = ""
        for i in range(33):
            l_abc += alpha.pop(random.randrange(0, len(alpha)))

    # Creating table
    b_abc = [l_abc]
    for i in range(32):
        l_abc = l_abc[1:] + l_abc[0]
        b_abc.append(l_abc)
    # Printing Alphabet
    # for i in range(len(b_abc)):
    #    print(b_abc[i])
    return b_abc


def coding(message: str) -> str:
    """
    Will code your text.
    :param message: text
    :return: str
    """
    # Code word
    ##################
    KEY = "МОСКВА"
    ##################
    global TAGS
    global alpha
    message = message.upper()
    # Coding message
    ans = ""
    for i in message:
        if i not in TAGS:
            ans += alpha[ord(i) - 1040][ord(KEY[0]) - 1040]
            KEY = KEY[1:] + KEY[0]
        else:
            ans += i
            KEY = KEY[1:] + KEY[0]
    return ans


def encoding(message: str) -> str:
    """
    Will encode your text.
    :param message: text
    :return: str
    """
    # Code word
    ##################
    KEY = "МОСКВА"
    ##################
    global alpha
    global TAGS
    ans = ""
    for i in message:
        for j in range(33):
            if i == alpha[ord(KEY[0]) - 1040][j]:
                ans += chr(1040 + j)
                KEY = KEY[1:] + KEY[0]
                break
            elif i in TAGS:
                ans += i
                KEY = KEY[1:] + KEY[0]
                break
    return ans


if __name__ == "__main__":
    TAGS = ",.?/!`~@#$%^&*()\|_+-='[]{}<>;:#  "
    alpha = alphabet(1)
    mess = str(input("Введите текст, который нужно закодировать: "))
    print(coding(mess))
    print(encoding(coding(mess)))
