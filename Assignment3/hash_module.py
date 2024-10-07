from Crypto.Hash import SHA256


class HashObject():
    def __init__(self):
        None

    def get_digest(self, uinput: str) -> hex:
        # A. Write a program that uses SHA256 to hash arbitrary inputs 
        #    and print the resulting digests to the screen in hexadecimal 
        #    format.
        hash_object = SHA256.new()
        hash_object.update(uinput.encode('utf-8'))

        return hash_object.hexdigest() 

