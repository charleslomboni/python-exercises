def reverse_str(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        r = f.read()
        with open("simply2.txt", "w", encoding="utf-8") as nf:
            nf.write(r[::-1])

reverse_str("simply.txt")