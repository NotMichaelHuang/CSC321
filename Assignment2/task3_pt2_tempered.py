from Assignment3Class.rsa import RSAKey

from Assignment3Class.CBC import CipherBlockChaining
from Assignment3Class.common_house import CommonHouse


def main():
    common_house = CommonHouse()
    rsa_algo = RSAKey()
    key = "Sixteen bytes"

    # t^e % n bob is giving it to alice
    c = rsa_algo.encrypt(key)

    # Mallory intercept
    c = 0

    # Alice's s = c'^d mod n
    s = rsa_algo.decrypt(c)
    s_bytes = s.to_bytes(1, 'big')

    m = 'Hi bob!'
    print("Encrypting message:", m)
    k = common_house.generate_hash(s_bytes)
    cbc = CipherBlockChaining(k)
    encrypted_msg = cbc.cbc_encrypt(m)

    # Hashes are deterministic and s yield 0 meaning k is SHA256 of 0
    # Save me some work and assume it is the same IV for CBC encryption as
    # for decryption
    decrypted_msg = cbc.cbc_decrypt(encrypted_msg)
    print(f"Mallory decrypted message: {decrypted_msg}")

    return 0


if __name__ == '__main__':
    main()

