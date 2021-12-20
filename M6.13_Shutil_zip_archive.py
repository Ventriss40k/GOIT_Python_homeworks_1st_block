import shutil

def create_backup(path,file_name,employee_residence):
    with open(f'{path}/{file_name}','wb') as fh:
        for data_key, data_val in employee_residence.items():
            fh.write((data_key+" "+data_val+ '\n').encode())
        archive_name = shutil.make_archive('backup_folder','zip',path)
        return archive_name