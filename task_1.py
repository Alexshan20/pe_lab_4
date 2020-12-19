import os


def get_files_count(dir: str) -> int:
    return len(os.listdir(path=dir))

files_count = get_files_count('C:/Users/alena/lab_4')
print(files_count)
