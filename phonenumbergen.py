''' Random phone number generator and text file creation
    Version 1.0
    Script FileName: phonenumbergen.py
    Supporting static areacodes for France, UK and Germany
    Created by: Mark Lawrence
    Data: Saturday 26 August 23
'''

import math
import random
import sys

try:
    country = str(sys.argv[1]).upper()  
except:
    print('Please set country argument on the command line.')
    print('Example: phonenumbergen.py UK, NETHERLANDS, SPAIN, FRANCE OR GERMANY')
    quit()

match country:
    case 'GERMANY':
        noLength = 12
        areaCodes = [4930,49521,49234,49421,49231,49351,49203,49211,49201,4969,4940,49511,49221,49341,4989,49911,49711,49202]
    case 'UK':
        noLength = 12
        areaCodes = [441273,441444,441903,44207,44161,44205,4479,441771,441785,441804,441908]
    case 'FRANCE':
        noLength = 11
        areaCodes = [331,332,333,334,335,336,337,338,339,3110,3120,31223,31486,3168]
    case 'NETHERLANDS':
        noLength = 11
        areaCodes = [31341,3138,31411,3145,31571,31524,]  
    case 'SPAIN':
        noLength = 11
        areaCodes = [34934,34912,34927,34945,34949,34958,34960,3471,3476,3477]        
    case _:
        print('Please set a valid country argument on the command line.')
        print('Example: phonenumbergen.py UK, NETHERLANDS, SPAIN, FRANCE OR GERMANY')
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

#CREATE RANDOM COUNTRY NUMBERS
with open('numbers.csv', 'w') as f:
    i=0
    requiredNumbers = 10000 #SET TO THE NUMBER OF RANDOM NUMBERS REQUIRED
    f.write('RANDOM')  #SET TO RANDOM, SEQUENTIAL, USER
    while i < requiredNumbers: 
        f.writelines('\n')
        f.writelines(e164randomNumber(noLength))
        
        i=i+1
    
    f.close()
    print (f'{requiredNumbers} records created for the country: {country}')