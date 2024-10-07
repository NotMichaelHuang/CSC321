from rsa import RSAKey

from CBC import CipherBlockChaining
from common_house import CommonHouse


def main():
    rsa_algo = RSAKey()
    key = 'Sixteen bytes'

    bob_to_alice = rsa_algo.encrypt(key)

    # Mallory temper
    mallory_key = bob_to_alice
    mallory_key = 0 

    # Decrypt key
    alice_bytes = rsa_algo.decrypt(mallory_key)

    m = 'Hi bob!'
    alice_key = CommonHouse().generate_hash(alice_bytes)
    common_algo = CipherBlockChaining(alice_key)
    alice_en = common_algo.encrypt(m)

    mallory_n = rsa_algo.get_n()
    mallory_e = rsa_algo.get_e()

    if(alice_key == 0):
        print("Mallory got the key")
    else:
        print("Alice key is different")


if __name__ == '__main__':
    main()

