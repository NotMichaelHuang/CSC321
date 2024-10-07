import os
from ECB import ElectronicCodeBook
from CBC import CipherBlockChaining
from task_two import SubmitVerify


def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')    # Window
        file_one = "Assignment1/cp-logo.bmp"
        file_two = "Assignment1/mustang.bmp"
    else:
        os.system('clear')  # MacOS or Linux
        file_one = "cp-logo.bmp"
        file_two = "mustang.bmp"

def electronic_codebook(opt_file: str) -> None:
    ecb = ElectronicCodeBook(opt_file)
    e_package = ecb.encrypt_bmp()
    ecb.export_encrypt_bmp(e_package)

def cipher_block_chaining(opt_pic: str) -> None:
    cbc = CipherBlockChaining(opt_pic)
    e_package = cbc.encrypt_bmp()
    cbc.export_encrypt_bmp(e_package)

def submit_verify(opt: int) -> None:
    sub_ver = SubmitVerify()
    encrypted_msg = sub_ver.submit()
    if(opt > 3):
        encrypted_msg = sub_ver.hacker_man(";admin=true", encrypted_msg)
    passed_status = sub_ver.verify(encrypted_msg)

    if passed_status:
        print("We been hacked!!!!!")
        exit()
    else:
        print("All is good...for now")
        exit()

def main() -> None:
    # Which encryption algorithm
    print("1. EBC")
    print("2. CBC")
    print("3. Task2")
    print("4. All your base are belong to us")
    user_input = int(input())
    clear_screen()

    # Spaghetti code incoming
    if user_input > 2:
        submit_verify(user_input)
        exit()  # Leave, I feel so ashamed writing code like this

    # Which image to use...
    print("1. cp-logo.bmp")
    print("2. mustang.bmp")
    opt_pic = int(input())

    if os.name == 'nt':
        file_one = "cp-logo.bmp"
        file_two = "mustang.bmp"
    else:
        file_one = "cp-logo.bmp"
        file_two = "mustang.bmp"

    # reassignment, a little curt but eh...
    if opt_pic == 1:
        opt_file = file_one
    else:
        opt_file = file_two

    if(user_input == 1):
        electronic_codebook(opt_file)
    else:
        cipher_block_chaining(opt_file)

if __name__ == "__main__":
    main()

