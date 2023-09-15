from task import Cipher


cipher = Cipher("Cryptopr")

print(cipher.encode("Hello world"))
# "Btggj vjmgp"
print(cipher.decode("Fjedhc dn atidsn"))
# "Kojima is genius"
