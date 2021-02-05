# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

cracked_password1 = password_cracker.crack_sha1_hash(
    "ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True)
print(cracked_password1)

cracked_password2 = password_cracker.crack_sha1_hash(
    "dcc466796201f7232b22a03781110a8871fd038c", use_salts=True)
print(cracked_password2)

cracked_password3 = password_cracker.crack_sha1_hash(
            "18c28604dd31094a8d69dae60f1bcd347f1afc5a")
print(cracked_password3)

# Run unit tests automatically
main(module='test_module', exit=False)
