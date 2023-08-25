import math
import random
import csv
import sys

try:
    country = str(sys.argv[1])
except:
    print('Please set country argument on command line.')
    print('Example: phonenumbergen.py UK')
    quit()

if country == 'germany' or country == 'Germany' or country == 'GERMANY':
    noLength = 12
    areaCodes = [4930,49521,49234,49421,49231,49351,49203,49211,49201,4969,4940,49511,49221,49341,4989,49911,49711,49202]
elif country == 'uk' or country == 'UK':
    noLength = 12
    areaCodes = [441273,441444,441903,44207,44161,44205,4479,441771,441785,441804,441908]
elif country == 'france' or country == 'France' or country == 'FRANCE':
    noLength = 11
    areaCodes = [331,332,333,334,335,336,337,338,339]
else:
    print('Please set a valid country argument on command line.')
    print('Example: phonenumbergen.py UK')
    quit()

def randomnumber(N):
	minimum = pow(10, N-1)
	maximum = pow(10, N) - 1
	return random.randint(minimum, maximum)

def e164randomNumber(noLength):
    areaCode = areaCodes[random.randint(0,len(areaCodes)-1)]
    digits = int(math.log10(areaCode))+1
    number = (randomnumber(noLength-digits))
    return f'+{areaCode}{number}'
f = open('numbers.csv', 'w')

writer = csv.writer(f)

i = 0
while i < 1000:
    writer.writerow([e164randomNumber(noLength)])
    i=i+1
    
f.close()

print (f'A thousand records created for country: {country}')