def no_dups(s):
    # Your code here
    splited_text = s.split()
    founded_text = []
    seen = set()

    for text in splited_text:
        if text not in seen:
            founded_text.append(text)
            seen.add(text)

    return ' '.join(founded_text)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))