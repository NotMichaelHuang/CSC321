import time
import matplotlib.pyplot as plt

from hash_module import HashObject


# B. Hash two strings (of any length) whose Hamming distance is exactly
#    1 bit (i.e. differ in ony 1 bit). Repeat this a few times.
# And C but I'm not writing all that
def two_strings_one_digest(digest_size: int, based_string: str):
    iterate = 0
    hashed = {}

    hasher = HashObject()

    start_time = time.time()
    while(True):
        modified_string = f"{based_string}_{iterate}"
        hash_obj = hasher.get_digest(modified_string)
        binary_hash = (bin(int(hash_obj, 16))[2:].zfill(256))[:digest_size]

        if binary_hash in hashed:
            print(f"Found collision on digest {digest_size}!!!")
            print("Digest 1: ", hashed[binary_hash])
            print("Digest 2: ", modified_string)
            print("Truncated Hash: ", binary_hash)

            end_time = time.time()
            delta_time = end_time - start_time
            return_list = [iterate, delta_time]
            return return_list
        else:
            hashed[binary_hash] = modified_string
            iterate += 1
        

def main():
    based_string = 'base_string'
    collision_attempts = []
    collision_times = []

    digest_size = list(range(8, 51, 2))
    for i in digest_size:
        # i es digest size
        digest_info = two_strings_one_digest(i, based_string)
        collision_attempts.append(digest_info[0])
        collision_times.append(digest_info[1])
    
    # Graph 1: Digest size vs. Collision time
    plt.figure()
    plt.plot(digest_size, collision_times, marker='o')
    plt.xlabel("Digest Size (bits)")
    plt.ylabel("Time to Collision (seconds)")
    plt.title("Digest Size vs. Time to Collision")
    plt.show()

    # Graph 2: Digest size vs. Number of inputs to collision
    plt.figure()
    plt.plot(digest_size, collision_attempts, marker='o')
    plt.xlabel("Digest Size (bits)")
    plt.ylabel("Number of Inputs to Collision")
    plt.title("Digest Size vs. Number of Inputs to Collision")
    plt.show()


if __name__ == "__main__":
    main()

