import random

from Assignment3Class.CBC import CipherBlockChaining
from Assignment3Class.common_house import CommonHouse
from Assignment3Class.diffie_hellman_eq import DiffieHellmanEquation


def main():
    # Parameters
    q = """B10B8F96 A080E01D DE92DE5E AE5D54EC 
            52C99FBC FB06A3C6 9A6A9DCA 52D23B61 
            6073E286 75A23D18 9838EF1E 2EE652C0 
            13ECB4AE A9061123 24975C3C D49B83BF 
            ACCBDD7D 90C4BD70 98488E9C 219A7372 
            4EFFD6FA E5644738 FAA31A4F F55BCCC0 
            A151AF5F 0DC8B4BD 45BF37DF 365C1A65 
            E68CFDA7 6D4DA708 DF1FB2BC 2E4A4371"""

    alpha = """A4D1CBD5 C3FD3412 6765A442 EFB99905 
                F8104DD2 58AC507F D6406CFF 14266D31 
                266FEA1E 5C41564B 777E690F 5504F213
                160217B4 B01B886A 5E91547F 9E2749F4 
                D7FBD7D3 B9A92EE1 909D0D22 63F80A76 
                A6A24C08 7A091F53 1DBF0A01 69B6A28A
                D662A4D1 8E73AFA3 2D779D59 18D08BC8 
                858F4DCE F97C2A24 855E6EEB 22B3B2E5"""

    # Convert hex to int
    q = q.replace(" ", "")
    q = q.replace("\n", "")

    alpha = alpha.replace(" ", "")
    alpha = alpha.replace("\n", "")
    
    integer_q = int(q, 16)
    integer_a = int(alpha, 16)

    # Stimulate 
    alice_number = random.randint(integer_a, integer_q)
    bob_number = random.randint(integer_a, integer_q)
    print(f"Alice private number {alice_number}")
    print(f"Bob private number {bob_number}")

    # Generate Alice/Bob class
    alice = DiffieHellmanEquation(alice_number)
    bob = DiffieHellmanEquation(bob_number)

    # Generate public keys and store them
    alice_pub = alice.public_key(integer_a, integer_q)
    bob_pub = bob.public_key(integer_a, integer_q)

    alice.set_public_key(alice_pub)
    bob.set_public_key(bob_pub)

    # Generate shared keys
    shared_alice = alice.get_shared_secret(integer_q, bob.public)
    shared_bob = bob.get_shared_secret(integer_q, alice.public)

    alice.set_shared_secret(shared_alice)
    bob.set_shared_secret(shared_bob)

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

    alice_decrypt_msg = common_algo.cbc_decrypt(alice_en)
    bob_decrypt_msg = common_algo.cbc_decrypt(bob_en)

    print(f"Alice Received: {alice_decrypt_msg}")
    print(f"Bob Received: {bob_decrypt_msg}")

    return 0


if __name__ == '__main__':
    main()

