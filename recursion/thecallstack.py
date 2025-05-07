def greet(name):
    print(f"Hello, {name} !")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

def greet2(name):
    print(f"How are you {name} ?")

def bye():
    print("Okay bye!")

if __name__ == "__main__":
    greet("Huy")