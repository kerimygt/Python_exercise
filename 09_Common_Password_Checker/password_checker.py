def password_check(password: str):
    with open("passwords.text", "r") as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f"{password} : ❌ (#{i})")
            return

    print(f"{password} : ✅ (Unique)")


user_password = input("Enter a password : ")
password_check(user_password)
