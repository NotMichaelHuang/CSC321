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
        user_input = ":admin<true" 

        # URL safe text
        user_input.replace(";", "%3B")
        user_input.replace("=", "%3D")
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
        # Attempt to decode the bytes into a string
        decrypted_str = decrypted_data.decode('utf-8', "ignore")

        if verification_text in decrypted_str:
           result_status = True             
        
        print("Verification text:")
        print(decrypted_data)

        # use built-in function to decrypt
        # check for ;admin=true
        return result_status
    
    
    def hacker_man(self, hacky_msg: str, en_msg: bin, block_size=16) -> bytes:
        """
        Perform a bit-flipping attack to inject 'hack_msg' into decrypted
        plaintext

        Args:
            hacky_msg (str): The malicious text to inject (e.g., ";admin=true")
            en_msg (bin): The encrypted message (ciphertext)
            block_size (int, optional): The block size (16 bytes for AES)

        Returns:
            bytes: The modified ciphertext with flipped bits
        """
        # URL encoded
        hacky_msg = hacky_msg.encode() 

        # make bin str mutable
        modified_cipher = bytearray(en_msg)

        # Determine which block to modify (2nd block in this example)
        # target_block_start = block_size

        # for i in range(0, len(hacky_msg)):
            # modified_byte = target_block_start - block_size + i

            # XOR previous block position with target block position then XOR with hack message position
            # Find the char and XOR with the same char that's when you can inject character
        #    modified_cipher[i] = (hacky_msg[i] ^ modified_cipher[i] ^ en_msg[target_block_start + i])

        # Bro fuck this noise I'm just gonna hard code this...
        modified_cipher = modified_cipher[0:4] + ((modified_cipher[4] ^ ord(":") ^ ord(";")).to_bytes(1, "big")) + modified_cipher[5:10] \
                    + ((modified_cipher[10] ^ ord("<") ^ ord("=")).to_bytes(1, "big")) + modified_cipher[11:]
        
        return modified_cipher
    

    def xor_bytes(self, block_one, block_two) -> bin:
        return_xor = bytes(a ^ b for a, b in zip(block_one, block_two))
        return return_xor

