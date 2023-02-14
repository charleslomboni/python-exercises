def write_file(text):
    
    f = open("simply.txt", "a", encoding="utf-8")
    f.write(text)
    f.close()

#write_file("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")

def reverse_str(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        r = f.read()
        with open("simply2.txt", "w", encoding="utf-8") as nf:
            nf.write(r[::-1])

reverse_str("simply.txt")