import base64

encrypted_flag_b64 = 'XWxPUD5HSBhAR1gHVnh9b31mNUg='
encrypted_flag = base64.b64decode(encrypted_flag_b64)

def decrypt(key, encrypted):
    key_length = len(key)

    cleartext = ''
    for i in range(0, len(encrypted)):
        j = i % key_length
        cleartext += chr(ord(key[j]) ^ ord(encrypted[i]))

    return cleartext

dictionary = open('dictionary.csv', 'r')
lines = dictionary.readlines()

cleartext = encrypted_flag.decode('UTF-8')
for line in lines:
    cleartext = decrypt(line.strip(), cleartext)
print(cleartext)