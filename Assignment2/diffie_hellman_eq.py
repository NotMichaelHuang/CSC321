import hashlib


class DiffieHellmanEquation():
    def __init__(self, private_number: int):
        self.private = private_number
        self.public = None
        self.shared_secret = None 


    # Get public keys from that....
    def public_key(self, alpha: int, p: int) -> int:
        return pow(alpha, self.private, p)


    def set_public_key(self, p_key: int) -> None:
        self.public = p_key

    # Generate shared secret and store them
    def get_shared_secret(self, p: int, other_pub: int) -> int:
        return pow(other_pub, self.private, p)
    
    def set_shared_secret(self, shared_secret: int) -> None:
        self.shared_secret = shared_secret

