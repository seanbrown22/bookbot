def main():
    
    bookname="Frankenstein"

    with open("books/frankenstein.txt") as f:
        file_contents=f.read()

    file_contents=file_contents.lower()
    character_count=len(file_contents)
    word_count=len(file_contents.split())
    print()
    print(f"Statistis for the book {bookname}")
    print("---------------------------------")
    print(f"Word count: {word_count}")
    print(f"Character count: {character_count}")
    from collections import Counter
    counters=Counter(file_contents)

    mykeys=list(counters.keys())
    mykeys.sort()
    sd={i:counters[i] for i in mykeys}
    print()
    print()
    print("Occurance of each specific character:")
    for letters in sd:
        numbers=sd[letters]
        print(f"{letters}: {numbers}")

    print("--- End of report ---")
    print()

main()
