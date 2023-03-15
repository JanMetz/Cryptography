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
        if len(str(elem)) >= minDigits:
            res.append(elem)

    return res


def pickPQ(primes):
    p = primes[random.randint(0, len(primes) // 2)]
    q = primes[random.randint(len(primes) // 2 + 1, len(primes))]

    return p, q


def generateEuler(phi):
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1:
            return e


def generateKeys(minDigits):
    primes = truncateResults(primeGenerator(int(minDigits * '2')), minDigits)
    p, q = pickPQ(primes)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generateEuler(phi)
    d = pow(e, -1, mod=phi)

    return (e, d, n)


def cipher(message, publicKey):
    if len(message) % 2:
        message = message + 'x'

    ciphered = []
    for i in range(0, len(message), 2):
        num = 1000 * ord(message[i]) + ord(message[i+1])
        ciphered.append(pow(num, publicKey[0], mod=publicKey[1]))

    return ciphered


def decipher(message, privateKey):
    deciphered = ''
    for i in message:
        num = pow(i, privateKey[0], mod=privateKey[1])
        deciphered += chr(num // 1000) + chr(num % 1000)

    return deciphered


def main():
    keys = generateKeys(7)
    publicKey = (keys[0], keys[2])
    privateKey = (keys[1], keys[2])

    msg = 'abcd'
    ciphered = cipher(msg, publicKey)
    print('original message: ', msg)
    print('ciphered: ', ciphered)
    print('deciphered: ', decipher(ciphered, privateKey))


if __name__ == '__main__':
    main()
