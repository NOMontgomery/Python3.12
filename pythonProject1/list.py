url = 'https://www.facebook.com/'
urls = ['https://twitter.com/home',
        'https://myspace.com/',
        'https://animefreak.video/',
        'https://www.animepro.de/',
        'https://www.gamespot.com/',

        ]

l = len(urls)
i = 0
while i < l:
    print(f'{urls [i]=}')
    i += 1

my_tuple = ['abcd', 78, 2.86, 'learnix', True, 'xyz']
my_list = ['abcd', 78, 2.86, 'learnix', True, 'xyz']
my_tinylist = [123, 'short']
empty_list = list()

print(my_list, my_tinylist[0], my_list[1:3], my_list[2:])
my_list.append('0')
print(f'{my_list=}')
my_tuple.append('0')
my_list[0] = 0
print(my_tuple)

print(F'{'\"=+"'}')
list(range(1, 11))
list(range(1, 10, 5))
print(range)
