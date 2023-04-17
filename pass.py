import secrets
import string

char_set=string.ascii_letters+string.hexdigits+string.digits+string.punctuation
n=int(input("pass of how much length"))
passw= ''.join(secrets.choice(char_set) for i in range(n))
print("ur new pass is" + passw)
