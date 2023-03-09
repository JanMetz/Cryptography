import random

def primeGenerator(M):
    result=[2,3]
    a=5
    b=7
    count=3
    factor=[5]       
    threshold=25     
    while a<M:
        if a==threshold:
            factor.append(result[count])
            threshold=factor[-1]**2
            count+=1
        elif all(a%k for k in factor):
            result.append(a)
        if b>=M:
            break
        elif b==threshold:
            factor.append(result[count])
            threshold=factor[-1]**2
            count+=1
        elif all(b%k for k in factor):
            result.append(b)
        a+=6
        b+=6
        
    return result

def truncateResults(dataset, minDigits):
    res = []

    for elem in dataset:
        if len(str(elem)) >= minDigits:
            res.append(elem)

    return res

def pickPQ(primes):
    p = primes[random.randint(0, int(0.5*len(primes)))]
    while p % 4 != 3:
        p = primes[random.randint(0, int(0.5*len(primes)))]
        
    q = primes[random.randint(int(0.5*len(primes)), len(primes))]
    while q % 4 != 3:
        q = primes[random.randint(int(0.5*len(primes)), len(primes))]

    return p, q

def generateNumbers():
    primes = truncateResults(primeGenerator(200000), 6)
    p, q = pickPQ(primes)
    n = p * q

    res = [primes[random.randint(0, len(primes))]**2 % n]

    for i in range(19999):
        res.append(res[-1]**2 % n)

    return res

def getRandomRow(row):
    res = []
    for elem in row:
        bits = 1 << 1
        res.append(elem & (bits - 1))
        
    return res

def occurencesTest(row):
    ones = 0
    for elem in row:
        if elem == 1:
            ones += 1

    if ones > 9725 and ones < 10275:
        return 'Passed'
    
    return 'Failed'

def seriesTest(row):
    series = [0]*7
    length = 0
    for elem in row:
        if elem == 1:
            length += 1
        else:
            if length >= 6:
                series[5] += 1
            else:
                series[length - 1] += 1

            length = 0

    if (series[0] > 2315 and series[0] < 2685 and
        series[1] > 1114 and series[1] < 1386 and
        series[2] > 527 and series[2] < 723 and
        series[3] > 240 and series[3] < 384 and
        series[4] > 103 and series[4] < 209 and
        series[5] > 103 and series[5] < 209):
            return 'Passed'
    
    return 'Failed'

def longSeriesTest(row):
    length = 0
    for elem in row:
        if elem == 1:
            length += 1
        else:
            if length >= 26:
                return 'Failed'

            length = 0

    return 'Passed'

def pokerTest(row):
    batch_size = 4
    keys = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
            '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    combinations_num = dict()

    for key in keys:
        combinations_num[key] = 0
        
    for i in range(len(row)// batch_size):
        batch = map(str, row[i * batch_size : (i + 1)* batch_size])
        key = str(''.join(batch))
        combinations_num[key] += 1

    sum = 0
    for val in combinations_num.values():
        sum += val ** 2

    x = sum * 16 / 5000 - 5000

    if x > 2.16 and x < 46.17:
        return 'Passed'
    
    return 'Failed'


def main():
    row = getRandomRow(generateNumbers())

    print('Tests Results')
    print('Occurence Test: ', occurencesTest(row))
    print('Series Test: ', seriesTest(row))
    print('26+ Series Test: ', longSeriesTest(row))
    print('Poker Test: ', pokerTest(row))


if __name__ == '__main__':
    main()
