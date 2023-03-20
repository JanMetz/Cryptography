import random
import math


def primeGenerator(M):
    result = [2, 3]
    a = 5
    b = 7
    count = 3
    factor = [5]
    threshold = 25
    while a < M:
        if a == threshold:
            factor.append(result[count])
            threshold = factor[-1] ** 2
            count += 1
        elif all(a % k for k in factor):
            result.append(a)
        if b >= M:
            break
        elif b == threshold:
            factor.append(result[count])
            threshold = factor[-1] ** 2
            count += 1
        elif all(b % k for k in factor):
            result.append(b)
        a += 6
        b += 6

    return result


def truncateResults(dataset, minDigits):
    res = []

    for elem in dataset:
        if elem % 2 and len(str(elem)) >= minDigits:
            res.append(elem)

    return res

  
def getPrimitiveRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if math.gcd(num, modulo) == 1}
    return [g for g in range(1, modulo // 10) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

  
def pickSharedData(primes):
    sharedBase = primes[random.randint(0, len(primes) - 1)] #n
    possibleSharedKeys = getPrimitiveRoots(sharedBase) #g
    
    return sharedBase, possibleSharedKeys[random.randint(0, len(possibleSharedKeys) - 1)]


def generateKeySet(sharedBase, sharedKey):
    privateKey = random.randint(1000, 9999)
    publicKey = sharedKey ** privateKey % sharedBase
    return privateKey, publicKey


def generateSessionKey(privateKey, otherPublicKey, sharedBase):
    return otherPublicKey ** privateKey % sharedBase


def main():
    print('Hold on! This may take a while...')
    minDigits = 3
    primes = truncateResults(primeGenerator(99999), minDigits)
    sharedBase, sharedKey = pickSharedData(primes)
    print(f'Shared Base (n): {sharedBase}\nShared key (g): {sharedKey}')
    
    privA, pubA = generateKeySet(sharedBase, sharedKey)
    print(f'User A private key: {privA} and public key: {pubA}')
    privB, pubB = generateKeySet(sharedBase, sharedKey)
    print(f'User B private key: {privB} and public key: {pubB}')
    
    kA = generateSessionKey(privA, pubB, sharedBase)
    kB = generateSessionKey(privB, pubA, sharedBase)
    if kA != kB:
        print('ERROR! GENERATED KEYS ARE DIFFERENT!')
        
    print(f'Session key (k): {kA}')

    
if __name__ == '__main__':
    main()
