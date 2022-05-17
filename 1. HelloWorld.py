s1 = "Hello World"
s2 = s1.replace(" ", "")
s2 = s1.upper()

cipher_and = [chr(ord(a) & 127) for a in (s1)]
cipher_or = [chr(ord(a) or 127) for a in (s1)]
cipher_xor = [chr(ord(a) ^ 127) for a in (s2)]
print("Logical AND operaton on string with 127 bits: ", "".join(cipher_and))
print("Logical OR operaton on string with 127 bits: ", "".join(cipher_or))
print("Logical XOR operaton on string with 127 bits: ", "".join(cipher_xor))
