#Telegram : string to morse code

morse_code = [
    '.-',       # A
    '-...',     # B
    '-.-.',     # C
    '-..',      # D
    '.',        # E
    '..-.',     # F
    '--.',      # G
    '....',     # H
    '..',       # I
    '.---',     # J
    '-.-',      # K
    '.-..',     # L
    '--',       # M
    '-.',       # N
    '---',      # O
    '.--.',     # P
    '--.-',     # Q
    '.-.',      # R
    '...',      # S
    '-',        # T
    '..-',      # U
    '...-',     # V
    '.--',      # W
    '-..-',     # X
    '-.--',     # Y
    '--..',     # Z
    '-----',    # 0
    '.----',    # 1
    '..---',    # 2
    '...--',    # 3
    '....-',    # 4
    '.....',    # 5
    '-....',    # 6
    '--...',    # 7
    '---..',    # 8
    '----.',    # 9
]

message = input('Enter the message : ').lower()
l1 = list(message)
print(l1)
a = ord('a')
converted_code =''
for i in l1:
    b = ord(i)
    c = b - a
    d = morse_code[c]
    converted_code += d
print('Morse code of the message is :',converted_code)
