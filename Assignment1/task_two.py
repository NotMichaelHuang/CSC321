import urllib.parse

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from common_house import CommonHouse


class SubmitVerify():
    def __init__(self):
        self.common_house = CommonHouse()

        self.key = b'Sixteen byte key'
        self.iv = get_random_bytes(16)

    def submit(self) -> bin:
        # Default user input
        user_input = urllib.parse.quote("Sixteen byte") # URL safe text
        prepend = "userid=456;userdata="
        append = ";session-id=31337"
        
        rtn_string = prepend + user_input + append
        padded_data = self.common_house.bmp_padding(rtn_string.encode())

        cipher = AES.new(self.key, AES.MODE_ECB)

        # I just got lazy so imma just copy and paste the CBC instead of 
        # modifying from django.utils.translation import pgettext_lazy
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
    

    def verify(self, en_msg: bin) -> bool:
        verification_text = ";admin=true"
        result_status = False

        # Decrypt the message
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

        decrypted_data = cipher.decrypt(en_msg)
        print(bytearray(decrypted_data))
        if bytearray(verification_text) in decrypted_data:
            print("True")
        else:
            print("False")
        import pdb; pdb.set_trace()
        try:
            # Attempt to decode the bytes into a string
            decrypted_str = decrypted_data.decode('utf-8', errors='ignore')
        except UnicodeDecodeError as e:
            print(f"Decode Error: {e}")
            return False  # Return False if decoding fails

        decrypted_data = urllib.parse.unquote(decrypted_str)

        if verification_text in decrypted_data:
           result_status = True             
        
        print("Verification text:")
        print(decrypted_data)

        # Unpad the message
        # use built-in function to decrypt
        # check for ;admin=true
        return result_status
    
    
    def hacker_man(self, hacky_msg: str, en_msg: bin, block_size=16) -> bin:
        # URL encoded
        # hacky_msg = urllib.parse.quote(hacky_msg).encode() 

        # make bin str mutable
        modified_cipher = bytearray(en_msg)

        target_block = 32 # bytes
        block_index = target_block // block_size    # 2
        offset_in_block = target_block % block_size # 0

        # Bit flipping
        for i in range(0, len(hacky_msg)):
            modified_byte = (block_index - 1) * block_size + offset_in_block + i
            modified_cipher[modified_byte - 1] ^= (ord(hacky_msg[i]) ^ en_msg[modified_byte])
        
        return modified_cipher
    

    def xor_bytes(self, block_one, block_two) -> bin:
        return_xor = bytes(a ^ b for a, b in zip(block_one, block_two))
        return return_xor

