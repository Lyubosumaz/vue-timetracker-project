import re

try:
    f = open('simple.txt', 'r')
    f.write('Test write to simple text!')
except IOError:
    print('ERROR: COULD NOT FIND FILE OR READ DATA!')
else:
    print('SUCCESS!')
    f.close()
finally:
    print('I ALWAYS WORK NO METTER WHAT!')

print('hello world')


patterns = ['term1', 'term2']
text = 'This is a stringdon with term1, but not the other'

# for pattern in patterns:
#     print("I'm seatching for: "+pattern)

#     if re.search(pattern, text):
#         print('MATCH!')
#     else:
#         print('NO MATCH!')

match = re.search(patterns[0], text)
print(type(match))
print(match.start())


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd'
test_patterns = ['sd*']

multi_re_find(test_patterns, test_phrase)
