from Assignment3Class.rsa import RSAKey

from Assignment3Class.CBC import CipherBlockChaining
from Assignment3Class.common_house import CommonHouse


def main():
    common_house = CommonHouse()
    rsa_algo = RSAKey()
    key = "Sixteen bytes"

    # t^e % n bob is giving it to alice
    c = rsa_algo.encrypt(key)

    # Mallory temper
    mallory_n = rsa_algo.get_n() # Modulo
    mallory_e = rsa_algo.get_e() # Common Prime

    # 2^e % n
    mallory_c = pow(2, mallory_e, mallory_n)

    # C_prime = C * 2^e -> (t^e * 2^e) % n 
    c_prime = c * mallory_c

    # (c_prime)^d = t * 2 mod n
    tempered_c = rsa_algo.decrypt(c_prime)

    #######################################################
    #     Mallory gonna reverse engineer the mfing key    #
    #######################################################
    original_c = tempered_c // 2
    if original_c == 0:
        original_hex = f"{0:02x}"
    else:
        original_hex = hex(original_c)
    
    original_hex = original_hex[2:]
    original_bytes = bytes.fromhex(original_hex)
    original_msg = original_bytes.decode("utf-8")

    import pdb; pdb.set_trace()


    m = 'Hi bob!'
    print("Encrypting message:", m)
    alice_key = common_house.generate_hash()
    common_algo = CipherBlockChaining(alice_key)


    return 0


if __name__ == '__main__':
    main()

