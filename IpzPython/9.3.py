MorzeCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}


def ConwerterToMorze(Stroka):
    lstA = [MorzeCode.get(i) for i in Stroka.upper() if i in MorzeCode]
    return ' '.join(lstA)


print(ConwerterToMorze(input("Enter the sentence you want to convert to Morse code.\n")))
