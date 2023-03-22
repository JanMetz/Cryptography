import hashlib
import time


def printHash(type, hash):
    print('The hexadecimal equivalent of provided message '\
          f'of {type} type hash is : {hash.hexdigest()}')

def readFile(filename):
    with open(filename, 'r') as f:
             return f.read().encode()

def printExeTime(start_time, end_time):
    elapsed = end_time - start_time
    if elapsed > 0.0:
        print(f'Execution time: {elapsed} seconds\n')
    else:
        print(f'Execution time: less than measuring precission\n')

def printMD5Hash(filename):
    start_time = time.time()
    result = hashlib.md5(readFile(filename))
    end_time = time.time()
    printHash('MD5', result)
    printExeTime(start_time, end_time)

def printSHA1Hash(filename):
    start_time = time.time()
    result = hashlib.sha1(readFile(filename))
    end_time = time.time()
    printHash('SHA1', result)
    printExeTime(start_time, end_time)

def printSHA256Hash(filename):
    start_time = time.time()
    result = hashlib.sha256(readFile(filename))
    end_time = time.time()
    printHash('SHA2_256', result)
    printExeTime(start_time, end_time)

def printSHA224Hash(filename):
    start_time = time.time()
    result = hashlib.sha224(readFile(filename))
    end_time = time.time()
    printHash('SHA2_224', result)
    printExeTime(start_time, end_time)

def printSHA384Hash(filename):
    start_time = time.time()
    result = hashlib.sha384(readFile(filename))
    end_time = time.time()
    printHash('SHA2_384', result)
    printExeTime(start_time, end_time)

def printSHA512Hash(filename):
    start_time = time.time()
    result = hashlib.sha512(readFile(filename))
    end_time = time.time()
    printHash('SHA2_512', result)
    printExeTime(start_time, end_time)

def printSHA3_256Hash(filename):
    start_time = time.time()
    result = hashlib.sha3_256(readFile(filename))
    end_time = time.time()
    printHash('SHA3_256', result)
    printExeTime(start_time, end_time)

def printSHA3_224Hash(filename):
    start_time = time.time()
    result = hashlib.sha3_224(readFile(filename))
    end_time = time.time()
    printHash('SHA3_224', result)
    printExeTime(start_time, end_time)

def printSHA3_384Hash(filename):
    start_time = time.time()
    result = hashlib.sha3_384(readFile(filename))
    end_time = time.time()
    printHash('SHA3_384', result)
    printExeTime(start_time, end_time)

def printSHA3_512Hash(filename):
    start_time = time.time()
    result = hashlib.sha3_512(readFile(filename))
    end_time = time.time()
    printHash('SHA3_512', result)
    printExeTime(start_time, end_time)

def printSHA2Hashes(filename):
    printSHA224Hash(filename)
    printSHA256Hash(filename)
    printSHA384Hash(filename)
    printSHA512Hash(filename)

def printSHA3Hashes(filename):
    printSHA3_224Hash(filename)
    printSHA3_256Hash(filename)
    printSHA3_384Hash(filename)
    printSHA3_512Hash(filename)

def printFileHashes(filename):
    content = readFile(filename)
    print(f'For string of length {len(content)} from file \'{filename}\':')
    print('\n*****MD5 HASHES*****\n')
    printMD5Hash(filename)

    print('\n*****SHA1 HASHES*****\n')
    printSHA1Hash(filename)

    print('\n*****SHA2 HASHES*****\n')
    printSHA2Hashes(filename)

    print('\n*****SHA3 HASHES*****\n')
    printSHA3Hashes(filename)

printFileHashes('file1.txt')
