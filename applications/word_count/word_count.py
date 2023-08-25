ignore = '":;,.-+=/\|[]{}()*^&'


def word_count(s):
    # Your code here
    result = {}
    filtered_text = [
        word.strip(ignore).lower()
        for word in s.split()
        if word.strip(ignore)
    ]
    for text in filtered_text:
        result[text] = result.get(text, 0) + 1

    return result


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
