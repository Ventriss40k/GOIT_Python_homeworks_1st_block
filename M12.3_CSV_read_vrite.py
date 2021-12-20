import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ["name","email","phone","favorite"]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow({"name":contact["name"],"email":contact["email"],"phone":contact["phone"],"favorite":contact["favorite"]})
    
def read_contacts_from_file(filename):
    with open (filename, "r", newline='') as fh:
        reader = csv.DictReader(fh)
        result =[]
        for row in reader:
            if row["favorite"]=="True":
                row["favorite"] = True
            elif row["favorite"]=="False":
                row["favorite"] = False
            result.append(row)
        return result
    

contacts =     [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Uick",
        "email": "uick.j@vestibul.co.uk",
        "phone": "(560) 914-3456",
        "favorite": True,
    }]
filename = "test_csv.csv"
write_contacts_to_file(filename, contacts)
# read_contacts_from_file(filename)
# print(type(read_contacts_from_file(filename)))
print(contacts == read_contacts_from_file(filename))
print(contacts)
print(read_contacts_from_file(filename))