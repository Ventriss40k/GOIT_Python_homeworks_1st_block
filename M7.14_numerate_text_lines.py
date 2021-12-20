start_file = "text.txt"
end_file = "numerated_lines_text.txt"
def to_indexed(start_file, end_file):
    new_lines =[]
    counter = 0
    with open(start_file, "r") as fh:
        lines = fh.readlines()
        for i in lines:
            new_lines.append(str(counter)+": " +str(i))
            counter +=1
        with open(end_file, "w") as fhw:
              fhw.writelines(new_lines)   
to_indexed(start_file, end_file)