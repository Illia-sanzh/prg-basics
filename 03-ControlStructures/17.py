plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char == ' ':
        encrypted_text += ' '
    else:
        char1 = ord(char) + 1
        encrypted_text += chr(char1)

print(plain_text)
print(encrypted_text)