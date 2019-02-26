import  hashlib, pyaes, os, rsa
# from transactions.models import Session
# from user.models import User
# Alright so before submitting string. must encode('utf-8')
# And before working with must hexdigest()

class livingDead(object):
    """
    This class handles all of the transactional encryption tomfoolery,
    Also, name taken from the tomb encryption tool
    """
    # utf-8 encode/decode twin functions
    def utfE(string):
            return string.encode('utf-8')
    def utfD(string):
        return string.decode('utf-8')


    class Zombie(object):
        """
        Zombie deals with symmetric encryption and hasing
        """
        # Hashes with sha512 & returns a string
        def hash(string):
            """
            Hashes the string
            """
            temp = livingDead.utfE(string)
            return hashlib.sha512(temp).hexdigest()

        # 256 bit key
        def genKey(length=32):
            """
            genereates a 256 bit key can substitute length though
            """
            return os.urandom(length)

        # Encryptsd
        def encrypt(text,key):
            """
            Enrypts string using aes key
            """
            aes = pyaes.AESModeOfOperationCTR(key)
            ciphertext = aes.encrypt(text)
            return ciphertext

        # Decrypts
        def decrypt(text,key):
            """
            Decrypts string using aes key
            """
            aes = pyaes.AESModeOfOperationCTR(key)
            decrypted = aes.decrypt(text)
            return decrypted

        # Will encrypt and return context
        def destroy(text):
            """
            generates keys and encrypts string
            """
            key = livingDead.Zombie.genKey()
            x = livingDead.Zombie.encrypt(text,key)
            context = {
            'key':  key,
            'text': text,
            'encryptedString': x
            }
            return context

        # Will decrypt and return bool
        def resurrect(text,key):
            y = livingDead.utfD(livingDead.Zombie.decrypt(text,key))
            if y == text:
                return True
            else:
                return False


    class Frankenstein(object):
        """
        Zombie deals with symmetric encryption and hasing
        """
        def genKeys():
            """
            Return rsa pub and priv keys
            """
            (pub, priv) = rsa.newkeys(256)
            context = {
            'pub': pub,
            'priv': priv
            }
            return context

        def encrypt(string,pub):
            """
        Encrypts string with pub
            """
            string = livingDead.utfE(string)
            crypto = rsa.encrypt(string, pub)
            return crypto

        def decrypt(crypto, priv):
            """
            Decrypts string with priv
            """
            string = rsa.encrypt(crypto, priv)
            string = livingDead.utfE(crypto)
            return crypto

        def findBrains():
            """
            Ths initializes and returns a context
            """
            keys = livingDead.Frankenstein.genKeys()
            return keys

        def eatBrains(text,priv):
            """
            This checks if decrypt is valid and all
            """
            y = livingDead.utfD(livingDead.Frankenstein.decrypt(text,key))
            try:
                return True
            except:
                return False
