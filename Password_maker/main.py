def make_password(phrase):
    return "".join([word[0] for word in phrase.split(" ")]).replace("o", "0").replace("O", "0").replace("i", "1").replace("I", "1").replace("s", "5").replace("S", "5")

if __name__ == '__main__':
    print(make_password("Give me liberty or give me death"))