from Crypto.Util import number


def find_d(phi: int, e: int):
    return pow(e, -1, phi)


def main():
    n_length = 2048

    p = number.getPrime(n_length)
    q = number.getPrime(n_length)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537 # 'Random' exponent

    # d * e mod phi = 1
    d = find_d(phi, e)

    # Get user input string -> Bin -> Hex -> integer (M)
    sample_text = "Hello World!"
    bin_text = sample_text.encode('utf-8')
    hex_text = bin_text.hex()
    int_text = int(hex_text, 16)

    # Encryption M^e % n (C)
    en_msg = pow(int_text, e, n)

    # Decryption C^d % n (DC)
    de_msg = pow(en_msg, d, n)
    hex_msg = hex(de_msg)
    # remove the 0x
    hex_msg = hex_msg[2:]
    bytes_msg = bytes.fromhex(hex_msg)
    bin_msg = bytes_msg.decode('utf-8')
    de_de_msg = bin_msg

    print(de_de_msg)

if __name__ == '__main__':
    main()

