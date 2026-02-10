import os 
import shutil
import datetime

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,"gztar" ,source)


source = r"C:\Users\hetpa\OneDrive\Documents\Desktop\AI"
destination = r"C:\Users\hetpa\OneDrive\Documents\Desktop\AI\backups"

backup_files(source,destination)