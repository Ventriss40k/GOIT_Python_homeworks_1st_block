import re
text = "fgg\nfdvf\fdf"
def real_len(text):
    new_str = re.sub(r'(\n|\f|\r|\t|\t)', "",text)
    return len(new_str)
print(real_len(text))

