from Crypto.Util import number


class RSAKey():

    def __init__(self):
        n_length = 2048

        self.p = number.getPrime(n_length)
        self.q = number.getPrime(n_length)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = 65537

        # d * e mod phi = 1
        self.d = pow(self.e, -1, self.phi)
    
    
    def get_n(self):
        return self.n

        
    def get_e(self):
        return self.e


    def encrypt(self, raw_key: str) -> int:
        # Get user input string -> Bin -> Hex -> integer (M)
        bin_text = raw_key.encode('utf-8')
        hex_text = bin_text.hex()
        int_text = int(hex_text, 16)

        # Encryption M^e % n (C)
        return pow(int_text, self.e, self.n)    


    def decrypt(self, key: int) -> int:
        # Decryption C^d % n (DC)`
        return pow(key, self.d, self.n) 
        
    
    def decrypt_to_str(self, int_msg: int) -> str:
        if int_msg == 0:
            hex_msg = f"{0:02x}" # Output 0x00
        else:
            hex_msg = hex(int_msg)
 
        # remove the 0x
        hex_msg = hex_msg[2:]
        bytes_msg = bytes.fromhex(hex_msg)
        bin_msg = bytes_msg.decode('utf-8')
        de_de_msg = bin_msg

        return de_de_msg 

