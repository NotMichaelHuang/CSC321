import random
from diffie_hellman_eq import DiffieHellmanEquation

def main():
    # Parameters
    p = 37
    alpha = 5

    # Stimulate 
    alice_number = random.randint(alpha, p)
    bob_number = random.randint(alpha, p)
    print(f"Alice private number {alice_number}")
    print(f"Bob private number {bob_number}")

    # Generate Alice/Bob class
    alice = DiffieHellmanEquation(alice_number)
    bob = DiffieHellmanEquation(bob_number)

    # Generate public keys and store them
    alice_pub = alice.public_key(alpha, p)
    bob_pub = bob.public_key(alpha, p)

    alice.set_public_key(alice_pub)
    bob.set_public_key(bob_pub)

    # Generate shared keys
    shared_alice = alice.get_shared_secret(p, bob_pub)
    shared_bob = bob.get_shared_secret(p, alice_pub)

    alice.set_shared_secret(shared_bob)
    bob.set_shared_secret(shared_alice)

    print(shared_alice, " ", shared_bob)

    import pdb; pdb.set_trace()

    return 0

if __name__ == '__main__':
    main()

