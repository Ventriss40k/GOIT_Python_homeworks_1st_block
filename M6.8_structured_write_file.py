source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output = "M6.8_output.txt"

def save_applicant_data(source, output):
    line = []
    output_text =''
    with open(output, "w") as fh:
        for i in source:

                for value in i.values():
                    value = str(value)
                    line.append(value)
                result = ",".join(line); result = result + "\n"
                output_text = output_text+result
                line.clear() 
        fh.write(output_text)
                 







save_applicant_data(source,output)
    
        
            
                
            