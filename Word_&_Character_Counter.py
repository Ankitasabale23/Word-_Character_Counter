# Word and Character Counter

text = input("Enter a paragraph: ")

if text.strip() == "":
    print("Input cannot be empty.")
else:
    # Count characters
    characters = len(text)

    # Count spaces
    spaces = text.count(" ")

    # Count words
    words = len(text.split())

    # Count sentences
    sentences = 0

    for char in text:
        if char in ".!?":
            sentences += 1

    print("\n----- Text Statistics -----")
    print("Characters:", characters)
    print("Words:", words)
    print("Sentences:", sentences)
    print("Spaces:", spaces)