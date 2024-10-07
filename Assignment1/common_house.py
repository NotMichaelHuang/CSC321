"""
This class houses the common functionality that both ECB and CBC would need....
Common functionality:
    Padding
    reading file types and preservation of such
"""
class CommonHouse():
    # No __init__ method here
    
    # preserve bmp header
    def bmp_preserve_header(self, file_type: str) -> list:
        bmp_header = None
        bmp_dib = None
        pixel_data = None

        # read data 
        try:
            with open(file_type, "rb") as bmp_data:
                # preserve bmp header 
                bmp_header = bmp_data.read(14)
                bmp_dib = bmp_data.read(40)
                pixel_data = bmp_data.read()   # Read the rest of the data
            
                gutted_bmp = [bmp_header, bmp_dib, pixel_data]
        except FileNotFoundError:
            print("File Name does not exist")
            exit()

        return gutted_bmp


    # Pad pixel data default 16
    def bmp_padding(self, pixel_data, block_size=16) -> bin:
        # Calculate the number of bytes needed to pad 
        padding_len = block_size - (len(pixel_data) % block_size)

        # 16 byes in AES standard format
        # It will generate a repeated a list of padding_len * padding_len
        padding = bytes([padding_len] * padding_len)
        padded_data = pixel_data + padding

        return padded_data

