from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)


class Encryptor():
     """Creates encryption key

     Args:
          None
     """

    def key_create(self):
        key = Fernet.generate_key()
        return key
    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)
        """This method will encrypt the file with the student info
        
        Args:
            key (key): the key to encyrpt the file
        """ 

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key
        """This method will decrypt the file with the student info

        Args:
            key (key): the key to decrypt the file
        """

    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()
        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)
        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
