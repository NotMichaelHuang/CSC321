from Crypto.Util import number
from Assignment3Class.rsa import RSAKey


def find_d(phi: int, e: int):
    return pow(e, -1, phi)


def main():
    rsa_algo = RSAKey()
    key = "Hello World!"
    print(f"Before encryption: {key}\n")

    en_msg = rsa_algo.encrypt(key) 
    print(f"Encrypted Message: \n {en_msg}\n")

    de_msg = rsa_algo.decrypt(en_msg)
    de_msg = rsa_algo.decrypt_to_str(de_msg)

    if key != de_msg: 
        raise ValueError("Invalid message")

    print(f"Decrypted Message: {de_msg}")     

if __name__ == '__main__':
    main()

