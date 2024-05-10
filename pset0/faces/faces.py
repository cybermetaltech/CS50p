# faces

# ask the user a sentence
# create a function called convert that replace :) with 🙂 and :( with 🙁
# create a function main that return the sentence with emoticons

def main():
    user = input()
    result = convert(user)
    print(result)


def convert(user):
    emoticon = user.replace(":)", "🙂").replace(":(", "🙁")
    return emoticon

main()
