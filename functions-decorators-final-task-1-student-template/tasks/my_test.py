from task import split


data = ['a b c\nf e r \n', ' ab a ', '  adf 5 7', '', '123', ',123,', ' ', 'adf<><>5asdf<>aasdf', 'adf<>5', 'adf   5 7',
        ' asdf \n5 7', ' adf 5 7', 'sdf sdfds   ssdf      ', 'a b c d']
sep = [' ', None, '\n', ',', '<>', '  ', '   ']
maxsplit = [-1, 2, 1, 0]

# data = [' asdf  5 7']
# sep = [None]
# maxsplit = [1]

for d in data:
    for s in sep:
        for m in maxsplit:
            a = split(d, sep=s, maxsplit=m)
            b = d.split(sep=s, maxsplit=m)
            if a != b:
                print('False')
                print(f'Date = "{d}"  |  sep = "{s}"  |  split = "{m}"')
                print(f'{a}  |  {b}')
