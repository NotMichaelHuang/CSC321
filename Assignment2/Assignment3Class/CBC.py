from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from .common_house import CommonHouse


class CipherBlockChaining():
    def __init__(self, key: bytes): 
        self.key = key
        self.iv = get_random_bytes(16)
        self.common_house = CommonHouse()
    
    def cbc_encrypt(self, msg: str) -> bytes:
        msg = msg.encode()

        # Scan for additional padding (bmp)
        padded_data = self.common_house.padding(msg) 

        # Generate a Cipher in CBC mode
        cipher = AES.new(self.key, AES.MODE_ECB)

        encrypted_data = b''
        priming_cipher_block = self.iv
        block_size = 16
        for i in range(0, len(padded_data), block_size):
            block_data = padded_data[i:i + block_size]
            xor_block = self.xor_bytes(block_data, priming_cipher_block)
            encrypted_block = cipher.encrypt(xor_block)

            encrypted_data += encrypted_block

            priming_cipher_block = encrypted_block

        return encrypted_data
    

    def back_door_key(self, key: bytes) -> None:
        self.key = key
    
    
    def cbc_decrypt(self, msg_en: bytes):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

        decrypted_data = cipher.decrypt(msg_en)
        decrypted_str = decrypted_data.decode()

        return decrypted_str

    
    def xor_bytes(self, block_one, block_two):
        return_xor = bytes(a ^ b for a, b in zip(block_one, block_two))
        return return_xor

