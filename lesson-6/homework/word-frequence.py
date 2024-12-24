import string
from collections import Counter

def word_frequency_counter():
    try:
        with open("sample.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File 'sample.txt' not found. Please create it.")
        text = input("Enter a paragraph to save in 'sample.txt': ")
        with open("sample.txt", "w") as file:
            file.write(text)

    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    total_words = len(words)
    word_counts = Counter(words)

    print(f"Total words: {total_words}")
    top_words = word_counts.most_common(5)
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")
    print("Word count report saved to 'word_count_report.txt'.")

    n = int(input("How many top words do you want to see? "))
    top_words = word_counts.most_common(n)
    print(f"Top {n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

word_frequency_counter()
