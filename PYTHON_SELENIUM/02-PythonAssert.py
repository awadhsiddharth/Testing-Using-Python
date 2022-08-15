def login():
    pin = input("Enter your PIN : ")
    assert pin == "1234", "Login Failed..."
    print("Login Success")

login()
