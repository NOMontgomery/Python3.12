urls = ['https://twitter.com/home',
        'https://myspace.com/',
        'https://animefreak.video/',
        'https://www.animepro.de/',
        'https://www.gamespot.com/',
        ]
for url in urls:
    print(f'{url=}')
print(f'{len(urls)}, {range(5)}, {list(range(len(urls)))}')
for i in range(1, len(urls)):
    print(f'{urls[i]=}')

l = len(urls)
r = range(l)
print(r)

for i in r:
    print(i)
