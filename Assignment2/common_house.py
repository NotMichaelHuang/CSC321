"""
This class houses the common functionality that both ECB and CBC would need....
Common functionality:
    Padding
    reading file types and preservation of such
"""
import hashlib


class CommonHouse():
    # Generate a 256 hash and then truncate it lol
    def generate_hash(self, input_data: bytes):
        sha256 = hashlib.sha256(input_data).digest()
        truncate_sha = sha256[:16]

        return truncate_sha


    # Pad pixel data default 16
    def padding(self, pixel_data, block_size=16) -> bin:
        # Calculate the number of bytes needed to pad 
        padding_len = block_size - (len(pixel_data) % block_size)

        # 16 byes in AES standard format
        # It will generate a repeated a list of padding_len * padding_len
        padding = bytes([padding_len] * padding_len)
        padded_data = pixel_data + padding

        return padded_data

