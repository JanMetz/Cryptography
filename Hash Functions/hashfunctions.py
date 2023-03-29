import hashlib
import time


def printHash(type, hash):
    type = type.replace('hashlib.', '')
    print(f'\tUsed hash function: {type}')
    print(f'\tLength of produced hash: {len(hash.hexdigest())}')


def readFile(filename):
    with open(filename, 'r') as f:
             return f.read().encode()


def printExeTime(start_time, end_time):
    elapsed = end_time - start_time
    if elapsed > 0.0:
        print(f'\tExecution time: {elapsed} seconds\n')
    else:
        print(f'\tExecution time: less than measuring precission\n')


def checkHash(filename, hashfun):
    file_content = readFile(filename)
    start_time = time.time()
    hashed = eval(hashfun)(file_content)
    end_time = time.time()
    printHash(hashfun, hashed)
    printExeTime(start_time, end_time)


def checkSHA2Hashes(filename):
    checkHash(filename, 'hashlib.sha224')
    checkHash(filename, 'hashlib.sha256')
    checkHash(filename, 'hashlib.sha384')
    checkHash(filename, 'hashlib.sha512')


def checkSHA3Hashes(filename):
    checkHash(filename, 'hashlib.sha3_224')
    checkHash(filename, 'hashlib.sha3_256')
    checkHash(filename, 'hashlib.sha3_384')
    checkHash(filename, 'hashlib.sha3_512')
    

def checkHashes(filename):
    print('\n*****NEW FILE*****\n')
    content = readFile(filename)
    print(f'For string of length {len(content)}:')

    print('\n*****SHA1 & MD5 HASHES*****\n')
    checkHash(filename, 'hashlib.md5')
    checkHash(filename, 'hashlib.sha1')

    print('\n*****SHA2 HASHES*****\n')
    checkSHA2Hashes(filename)

    print('\n*****SHA3 HASHES*****\n')
    checkSHA3Hashes(filename)
    
    print('\n*****END*****\n')


def checkStrictAvalancheCriterium():
    hashed1 = hashlib.sha3_512('11101101010101010101101100101'.encode()).hexdigest()
    hashed2 = hashlib.sha3_512('11101101010101110101101100101'.encode()).hexdigest()

    if len(hashed1) != len(hashed2):
        print('Produced hashed have different length!')
        return

    compliant_num = 0
    for i in range(len(hashed1)):
        if hashed1[i] == hashed2[i]:
            compliant_num += 1

    compliant_proc = compliant_num / len(hashed1)
    if  compliant_proc < 0.5:
        print('Avalanche Criterium Test For SHA3_512 Passed!')
              
    else:
        print('Avalanche Criterium Test For SHA3_512 Failed!')
        
    print(f'Percent of bits that have not changed: {compliant_proc}')


def hashUserInput():
    hash_functions = ['sha224', 'sha256', 'sha384', 'sha512',
                      'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
                      'sha1', 'md5']
    
    print(f'Pick hash function: {hash_functions}')
    hash_function = input()

    while hash_function not in hash_functions:
        print('Invalid hash function picked. Please try again')
        hash_function = input()

    print('Provide message, that you want to hash: ')
    msg = input().encode()
    
    hashed = eval('hashlib.' + hash_function)(msg).hexdigest()
    print(f'Your message after hasing is: {hashed}')


def profileHashFunctions():
    input_files = ['file1.txt', 'file2.txt']
    for file in input_files:
        checkHashes(file)

def checkForCollisions():
    pass


def main():
    dct = {'1': 'hashUserInput', '2': 'profileHashFunctions', '6': 'checkStrictAvalancheCriterium'}
    keys = list(dct.keys())
    
    print(f'Which part of this app would you like to launch? {dct}')

    opt = input()
    while opt not in keys:
        print(f'Wrong option chosen {opt} not in {keys}! Try again')
        opt = input()

    eval (dct[opt])()


if __name__ == '__main__':
    main()
