import hashlib

def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()

    return digest

def main():
    user_input_SHA1 = input("Enter the SHA1 to be Cracked: ")
    cleaned_input_SHA1 = user_input_SHA1.strip().lower()

    with open('passwords.txt') as g:
        for line in g:
            password = line.strip()
            convert_SHA1 = convert_text_to_sha1(password)

            if cleaned_input_SHA1 == convert_SHA1:
                print (f"Password Found: {password}")
                return

    print ("Could not find the passwords")


if __name__ == '__main__':
    main()
