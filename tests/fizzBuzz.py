for i in range(1, 101):
    fb_str = ""
    if i % 3 == 0:
        fb_str += "Fizz"
    if i % 5 == 0:
        fb_str += "Buzz"
    if fb_str == "":
        fb_str += str(i)
    print(fb_str)
