import random

from CBC import CipherBlockChaining
from common_house import CommonHouse
from mallory import Mallory
from diffie_hellman_eq import DiffieHellmanEquation


def main():
    alphas = [1, 5, 36, 37]
    for i in range(0, 3):
        # Parameters
        integer_q = 37
        integer_a = alphas[i]

        # Stimulate 
        alice_number = random.randint(integer_a, integer_q)
        bob_number = random.randint(integer_a, integer_q)
        print(f"Current alpha: {integer_a}")
        print(f"Alice private number {alice_number}")
        print(f"Bob private number {bob_number}")

        # Generate Alice/Bob class
        alice = DiffieHellmanEquation(alice_number)
        bob = DiffieHellmanEquation(bob_number)

        # Generate public keys and store them
        alice_pub = alice.public_key(integer_a, integer_q)
        bob_pub = bob.public_key(integer_a, integer_q)

        # Inject q into both alice and bob...
        mallory = Mallory(integer_q)
        mallory.set_alice_pub(alice_pub)
        mallory.set_bob_pub(bob_pub)

        alice.set_public_key(mallory.sleeper)
        bob.set_public_key(mallory.sleeper)

        # Generate shared keys
        shared_alice = alice.get_shared_secret(integer_q, bob.public)
        shared_bob = bob.get_shared_secret(integer_q, alice.public)

        alice.set_shared_secret(shared_alice)
        bob.set_shared_secret(shared_bob)

        #################################################################
        #   Mallory gonna crack the private key and get shared_secret   #
        #################################################################
        mallory.break_alice_private(integer_a, integer_q)
        mallory.break_bob_private(integer_a, integer_q)    
        mallory.acquire_secret()

        # Generate Hash or Key
        alice_size = (alice.shared_secret.bit_length() + 7 // 8) # The correct byte size
        bob_size = (bob.shared_secret.bit_length() + 7 // 8)

        alice_bytes = alice.shared_secret.to_bytes(alice_size, byteorder='big')
        bob_bytes = bob.shared_secret.to_bytes(bob_size, byteorder='big')

        alice_key = CommonHouse().generate_hash(alice_bytes)
        bob_key = CommonHouse().generate_hash(bob_bytes)

        if alice_key != bob_key:
            print("Invalid key generation")
            print(f"Alice:{alice_key}")
            print(f"Bob:{bob_key}")

        # Generate and encrypt message
        bob_msg = "Hi Alice"
        alice_msg = "Hi Bob"

        # This should be the same key so it does not matter bob or alice...
        common_algo = CipherBlockChaining(alice_key)
        alice_en = common_algo.cbc_encrypt(bob_msg)
        bob_en = common_algo.cbc_encrypt(alice_msg)

        #################################################################
        #               Decrypt alice and bob's messages                #
        #################################################################
        alice_decrypt_msg = common_algo.cbc_decrypt(alice_en)
        bob_decrypt_msg = common_algo.cbc_decrypt(bob_en)

        print("\n***************************")
        print("* What Alice and Bob sees *")
        print("***************************")
        print(f"Alice Received: {alice_decrypt_msg}")
        print(f"Bob Received: {bob_decrypt_msg}")


        # Mallory's turn hehe

        # Too big brain
        # mallory_size = (mallory.secret.bit_length() + 7 // 8)
        # mallory_bytes = mallory.secret.to_bytes(mallory_size, byteorder='big')
        predictable_shared = 0
        predictable_shared = predictable_shared.to_bytes(0, 'big')
        mallory_key = CommonHouse().generate_hash(predictable_shared)

        mallory_algo = common_algo
        mallory_algo.back_door_key(mallory_key)
        alice_hacked = mallory_algo.cbc_decrypt(alice_en)
        print(f"M'Alice received: {alice_hacked}")
        bob_hacked = mallory_algo.cbc_decrypt(bob_en)
        print(f"M'Bob received: {bob_hacked}")

    return 0


if __name__ == '__main__':
    main()

