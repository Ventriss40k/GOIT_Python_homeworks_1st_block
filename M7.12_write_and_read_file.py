path = "text.txt"
additional_info="additional_info"
start_pos =1
count_chars =3
def file_operations(path, additional_info, start_pos, count_chars):
    with open(path,"a") as fh:
        fh.write(additional_info)
    with open(path,"r") as fh:
        fh.seek(start_pos)
        print(fh.read(count_chars))
        # print(fh.read(count_chars))












file_operations(path, additional_info, start_pos, count_chars)
