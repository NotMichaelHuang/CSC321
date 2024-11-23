from Assignment3Class.rsa import RSAKey

from Assignment3Class.CBC import CipherBlockChaining
from Assignment3Class.common_house import CommonHouse


def main():
    """
    Math:

    s1 = m1^d mod n
    s2 = m2^d mod n

    s3 = (s1 * s2) mod n

    s3^e mod n = (s1 * s2)^e mod n
    (m1^d * m2^d)^e mod n -> (m1 * m2)^(d * e) mod n

    d * e = 1 mod phi(n)

    m3 mod n
    Q.E.D s3 is a valid for m3 = m1 * m2 
    """
    # Parameters of RSA (for simplicity, we use small numbers; 
    # in real RSA, n is very large)
    n = 33  # modulus
    d = 3   # private key (exponent)
    e = 7   # public key (exponent, d * e ≡ 1 mod φ(n))

    # Messages Mallory sees and their signatures
    m1 = 4  # message 1
    m2 = 9  # message 2

    # Signatures for m1 and m2
    s1 = pow(m1, d, n)  # s1 = m1^d mod n
    s2 = pow(m2, d, n)  # s2 = m2^d mod n

    # Mallory constructs a new message m3
    m3 = (m1 * m2) % n

    # Mallory creates a new signature s3
    s3 = (s1 * s2) % n

    # Verify if s3 is a valid signature for m3
    # Verification: s3^e mod n should equal m3
    verification = pow(s3, e, n) == m3

    (s1, s2, m3, s3, verification)
    print("S1: ", s1)
    print("S2: ", s2)
    print("M3: ", m3)
    print("S3: ", s3)
    print("Verification: ", verification)

    return 0


if __name__ == '__main__':
    main()

