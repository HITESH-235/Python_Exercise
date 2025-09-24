#ROMAN TO INTEGER
#LEETCODE link: https://leetcode.com/problems/roman-to-integer/description/

def Roman(str):
    dct = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    integer = dct[str[-1]]
    for i in range(len(str)-1):
        if dct[str[i]] < dct[str[i+1]]:
            integer -= dct[str[i]]
        else:
            integer += dct[str[i]]
    return integer

print(Roman("MCMLXXXIV"))
