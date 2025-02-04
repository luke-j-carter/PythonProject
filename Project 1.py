import base64    # for encoding/decoding encrypted messages and signatures
import random    
import math

class RSACryptosystem:
    def __init__(self):
        """
        # intializing the RSA system and generating the intial key pair
        # p, q: prime numbers
        # n: public modulus (p * q)
        # phi: euler's totient function value
        # e: public exponent, d: private exponent (inverse of e)
        # public_key: tuple of (e, n)
        # private_key: tuple of (d, n)
        """
        
        selp.p = None
        self.q = None
        self.n = None
        self.e = None
        self.d = None
        self.public_key = None
        self.private_key = None

        # generate a key pair
        self_generate_keys()

def is_prime(self, num):
    """ is the given number prime
    argumnets: num (int) check if prime
    returns: (bool) true if prime, OTW flase
    """
    if num < 2:
        return False
        for i in range(2, int(math.sqrt(num) + 1):
            if num % i == 0;
            return False
        return True

def generate_prime(self, min=100, max=10000):
    """ generate a random prime
    returns: (int) random prime
    """

while True:
    num = random.randint(min, max)
    if self.is_prime(num):
        return num

def gcd(self, a, b):
    """ calculating gcd using the euclidean algorithm
    returns: (int) gcd of a and b
    """

while b:
    a, b = b, a % b
 return a

def mod_inverse(self, a, m):
    """ calculate modular inverse using the same algorithm ^^
    returns (int) modular multiplicative inverse
    raises: exception if the inverse DNE
    """
def extended_gcd(a.b):
    # internal recursive extended GCD
    if a == 0;
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

gcd, x, _ = extended_gcd(b % a, a)
if gcd != 1;
    raise Exception('Modular inverse DNE')
else:
    return x % m

        
def generate_keys(self):
    """ generate RSA public and private key pair
    generate 2 prime numbers
    calculate n and phi
    select the e
    calculate d
    store the tuples
    """

    # 2 primes
    self.p = self.generate_prime()
    while True:
        self.q = self.generate_prime()
        if self.p != self.q:
            break

    # calculate n and phi
    self.n = self.p  * self.q
    self.phi = (self.p - 1) * (self.q - 1)

    # choose public exponent
    self.e = random.randint(2, self.phi - 1)
    while self.gcd(self.e, self.phi) != 1:
        self.e = random.randint(2, self.phi - 1)

    # calculate exponent
    self.d = self.mod_inverse(self.em self.phi)

    # store the keys
    self.public_key = (self.e, self.n)
    self.private_key = (self.d, self.n)

def encrypt(self, message):
    """ encrypt a message using the public key
    message (str) message to encrypt
    returns (str) base64 encoded encrypted message
    """

    # convert the messege to a numeric representation
    numeric_message = [ord(char) for char in message]
    # encrypt each characters using the public key
    encrypted = []
    for char_num in numeric_message:
        encrypted_num = pow(char_num, self.public_key[0], self.public_key[1]0
        encrypted.append(encrypted_num)

    # encode and return as base64 string
    return base64.b64encode(bytes(str(encrypted), 'utf-8')).decode()


def decrypt(self, encrypted_message):
    """ decrypt a message using the private key
    encrypted_message (str) base64 message
    returns: (str) decrypted original message
    """

    # decode base64 message
    decoded = base64.b64decode(encrypted_message).decode()
    # convert back to the list of numbers
    encrypted_nums = eval(decoded)
    # decrypt each number using private key
    decrypted = []
    for enc_num in encrypted_nums:
        decrypted_num = pow(enc_num, self.private_key[0], self.private_key[1])
        decrypted.append(chr(decrypted_num))
    return ''.join(decrypted)




def clientInterface():
    encryptedList = []
    generateKeys()

    while True:
        userType = getUserType()

        if userType == "1":  # Public user
            handlePublicUser(encryptedList)
        elif userType == "2":  # Owner of keys
            handleOwnerOfKeys(encryptedList)
        elif userType == "3":  # Exit program
            print("Bye for now!")
            break
        else:
            print("Invalid choice.")


def getUserType():
    print("Please select your user type:\n"
          "\t1. A public user\n"
          "\t2. The owner of the keys\n"
          "\t3. Exit Program\n")
    return input("Enter your choice:")


def handlePublicUser(encryptedList):
    while True:
        print("As a public user, what would you like to do?\n"
              "\t1. Send an encrypted message\n"
              "\t2. Authenticate a digital signature\n"
              "\t3. Exit\n")
        publicUserSelection = input("Enter your choice:")

        if publicUserSelection == "1":
            encryptedMessage = input("Enter a message:")
            encryptedList.append(encryptedMessage)
            print("Message encrypted and sent.")
        elif publicUserSelection == "2":
            print("There are no signatures to authenticate.")
        elif publicUserSelection == "3":
            break
        else:
            print("Invalid choice.")


def handleOwnerOfKeys(encryptedList):
    while True:
        print("As the owner of the keys, what would you like to do?\n"
              "\t1. Decrypt a received message\n"
              "\t2. Digitally sign a message\n"
              "\t3. Show the keys\n"
              "\t4. Generate a new set of keys\n"
              "\t5. Exit\n")
        ownerSelection = input("Enter your choice:")

        if ownerSelection == "1":
            decryptMessage(encryptedList)
        elif ownerSelection == "2":
            print("There are no signatures to authenticate.")
        elif ownerSelection == "3":
            showKeys()
        elif ownerSelection == "4":
            generateNewKeys()
        elif ownerSelection == "5":
            break
        else:
            print("Invalid choice.")


def decryptMessage(encryptedList):
    if not encryptedList:
        print("No messages to decrypt.")
        return
    print("The following messages are available:")
    displayOptions(encryptedList)
    userEncryptedMessageChoice = int(input("Enter your choice:"))

    if 1 <= userEncryptedMessageChoice <= len(encryptedList):
        selectedMessage = encryptedList[userEncryptedMessageChoice - 1]
        print(f"You selected {userEncryptedMessageChoice}. This is the decrypted message: {selectedMessage}")
    else:
        print("Invalid choice.")


def showKeys():
    # Implement key display logic here (update the `keys` list accordingly)
    keys = ["Public Key", "Private Key"]  # Example keys
    displayOptions(keys)


def generateNewKeys():
    print("Generating a new set of keys...")
    generateKeys()


def displayOptions(options):
    for idx, option in enumerate(options):
        print(f"{idx + 1}.\t{option}")



clientInterface()
