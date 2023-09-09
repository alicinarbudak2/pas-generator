import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Şifre uzunluğunu girin: "))
        if password_length <= 0:
            raise ValueError("Geçersiz uzunluk")
        
        password = generate_password(password_length)
        print("Oluşturulan şifre:", password)
    except ValueError as e:
        print("Hata:", e)
