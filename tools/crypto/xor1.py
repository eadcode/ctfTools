import base64

encrypted_flag_b64 = 'jLL7+efO3NijndPfppLD5qWM2M2vy4/brg=='
encrypted_flag = base64.b64decode(encrypted_flag_b64)

# cafebabe
key = b'\xca\xfe\xba\xbe'

print('key -> ' + str(key))
print('encrypted_flag -> ' + str(encrypted_flag))
key_length = len(key)

cleartext = ''
for i in range(0, len(encrypted_flag)):
    j = i % key_length
    cleartext += chr(key[j] ^ encrypted_flag[i])
    
print(cleartext)