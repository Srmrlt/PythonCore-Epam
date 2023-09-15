from task import *


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Author='William Faulkner', Name='The Sound and the Fury', Price='12'
print('-------------------------------------------------------------------------')
# b.author = "new author"  # => ValueError: Author can not be changed.
# b.name = "new name"      # => ValueError: Name can not be changed.
b.price = 4
print(b.price)

