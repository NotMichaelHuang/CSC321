class Mallory():
    def __init__(self, q: int):
        self.alice_pri = None
        self.alice_pub = None

        self.bob_pri = None
        self.bob_pub = None

        self.secret = None

        self.sleeper = q
    
    
    def set_alice_pub(self, alice_pub: int) -> None:
        self.alice_pub = alice_pub

    
    def set_bob_pub(self, bob_pub: int) -> None:
        self.bob_pub = bob_pub

        
    def break_alice_private(self, alpha: int, q: int) -> None:
        self.alice_pri = self.brutal_force_private(alpha, q, self.alice_pub)
    
    
    def break_bob_private(self, alpha: int, q: int) -> None:
        self.bob_pri = self.brutal_force_private(alpha, q, self.bob_pub)

    
    def acquire_secret(self) -> None:
        alice_secret = pow(self.bob_pub, self.alice_pri, self.sleeper)
        bob_secret = pow(self.alice_pub, self.bob_pri, self.sleeper)

        if alice_secret == bob_secret:
            self.secret = alice_secret
        else:
            raise("Error: secret not matching...")

    
    def brutal_force_private(self, alpha: int, q: int, public_key: int) -> int:
        person = False 
    
        # Brutal force tf out of this...to get private key
        for i in range(alpha, q):
            pot_pub_key = pow(alpha, i, q)
            if pot_pub_key == public_key:
                person = i
                break
        return person
    
    