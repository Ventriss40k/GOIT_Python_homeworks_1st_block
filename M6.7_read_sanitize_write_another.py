import re
source = "to_sanitize.txt"
output = "sanitized.txt"
def sanitize_file(source, output):
    with open (source, "r") as fh:
        raw_text = fh.read()
        print(raw_text)
        sanitized_text = re.sub("[0-9]","",raw_text)
        print(sanitized_text)
    with open(output,"w") as fh:
        fh.write(sanitized_text)
        
        





sanitize_file(source, output)