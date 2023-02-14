def reverse_str(file_to_read, file_to_write):
    with open(file_to_read, "r", encoding="utf-8") as f:
        r = f.read()
        with open(file_to_write, "w", encoding="utf-8") as nf:
            nf.write(r[::-1])

reverse_str("simply.txt", "out.txt")