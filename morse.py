
morse = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e': '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm': '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-', 
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    # . : '.-.-',
    # , : '--..--',
    # ? : '..--..',
    # / : '--..-.',
    # @ : '.--.-.',
    # 1 : '.----',
    # 2 : '..---',
    # 3 : '...--',
    # 4 : '....-',
    # 5 : '.....',
    # 6 : '-....',
    # 7 : '--...',
    # 8 : '---..',
    # 9 : '----.',
    # 0 : '-----',
}


def ubah(tekss):
    # print(tekss.isalpha())
    if tekss.upper() == tekss.lower():
        kalimat = tekss.split(' / ')
        hasil = ''
        for i in kalimat:
            hasil += list(morse.keys())[list(morse.values()).index(i)]
        print(hasil)
    else :
        kalimat = tekss.lower().replace(' ', '')
        hasil = ''
        for i in kalimat:
                hasil+= morse[i] + '/'
        print(hasil)

# hari ke 6
