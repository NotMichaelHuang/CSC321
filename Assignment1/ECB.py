import os

from Crypto.Cipher import AES

from common_house import CommonHouse


class ElectronicCodeBook():
    def __init__(self, r_data: str):
        self.r_data = r_data
        self.key = b'Sixteen byte key' # 128-bit there are 16 char
        self.common_house = CommonHouse()
        
       
    def encrypt_bmp(self) -> list:
        # Saving header
        gutted_bmp = []
        gutted_bmp = self.common_house.bmp_preserve_header(self.r_data)        

        #indices
        header_index = 0
        dib_index = 1
        pixel_index = 2

        bmp_header = gutted_bmp[header_index]
        bmp_dib = gutted_bmp[dib_index]
        pixel_data = gutted_bmp[pixel_index]

        # Scan for additional padding (bmp)
        padded_data = self.common_house.bmp_padding(pixel_data) 
        
        # Create cipher from key in ECB mode
        cipher = AES.new(self.key, AES.MODE_ECB); 

        encrypted_data = b''
        block_size = 16
        for i in range(0, len(padded_data), block_size):   
            # i:i means the current head of the block and we are adding
            # additional length for a 16-byte (128-bit) encryption 
            current_block = padded_data[i:i + block_size]
            encrypted_block = cipher.encrypt(current_block)
            encrypted_data += encrypted_block 

        
        loose_data = [bmp_header, bmp_dib, encrypted_data]

        return loose_data    


    def export_encrypt_bmp(self, e_package: list) -> None: 
        bmp_header = 0
        bmp_dib = 1
        e_data = 2

        # Read encrypt data with header into a new file or something...
        #if os.name == 'nt': 
        #    comp_name = self.r_data.split('/')
        #    encrypted_name = "Assignment1/" + "en_" + comp_name[1]
        # else: 
        encrypted_name = "en_" + self.r_data

        with open(encrypted_name, "wb") as en_bmp_file:
            en_bmp_file.write(e_package[bmp_header])
            en_bmp_file.write(e_package[bmp_dib])
            en_bmp_file.write(e_package[e_data])   

        return None 

