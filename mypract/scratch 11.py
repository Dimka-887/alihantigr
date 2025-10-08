with open("hello.txt", "w") as file:
    file.write("hello world")

print("hello world")
with open("hello.txt", "a") as file:
    file.write("hello work")

print("hello work")
lines = ["Hello word\n" , "Hello work\n", "Hello world\n"]
with open("hello2.txt", "a") as file:
