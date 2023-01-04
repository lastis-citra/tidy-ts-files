import os

import unicodedata


def tidy_dir(path):
    dir_name_list = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    print(dir_name_list)
    file_name_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(file_name_list)

    for dir_name in dir_name_list:
        for file_name in file_name_list:
            if unicodedata.normalize('NFKC', dir_name) in unicodedata.normalize('NFKC', file_name):
                new_dir_path = os.path.join(path, dir_name)
                if os.path.exists(os.path.join(new_dir_path, file_name)):
                    print(f'ERROR!! "{file_name}" is already exists in [{new_dir_path}]!')
                    continue
                print(f'Moving "{file_name}" to [{new_dir_path}]')
                os.rename(os.path.join(path, file_name), os.path.join(new_dir_path, file_name))


if __name__ == '__main__':
    tidy_dir(os.environ['TIDY_PATH'])
