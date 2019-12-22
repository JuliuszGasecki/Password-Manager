import PasswordGenerator as generator
import Encryptor as enc

password_generator = generator.Password_generator()
password = password_generator.generate_password()
encryptor = enc.Encryptor()
en = encryptor.encrypt_aes(password)
print(en)
de = encryptor.decrypt_aes(en)
print(de)