import pathlib
import shutil
from pathlib import Path
import random


def list_roulette(inp_l: list, max_files: int) -> list:
    num_of_elements = random.randint(1, min(max_files, len(inp_l)))
    random.shuffle(inp_l)
    return inp_l[:num_of_elements]


def folder_filler(path, fil_path, number_of_folders, max_deep_of_subfolders, max_files):
    """

    :param path: path of the folder, where subfolderd would be generated. Could be str or Purepath
    :param fil_path: path of the folder, containing files library
    :param number_of_folders: number of 1st level subfolders
    :param max_deep_of_subfolders: max amount of nested folders
    :param max_files: max amount of files in each folder
    :return:
    """
    list_of_files = list(fil_path.glob('*/'))
    for i in range(1, number_of_folders + 1):
        deep = random.randint(1, max_deep_of_subfolders)
        subpath = path / str(i)
        subpath.mkdir()
        for filepath in list_roulette(list_of_files, max_files):
            shutil.copy(str(filepath), str(subpath))
        for j in range(1, deep + 1):
            subpath = subpath / (str(i)+'.'+str(j))
            subpath.mkdir()
            for filepath in list_roulette(list_of_files, max_files):
                shutil.copy(str(filepath), str(subpath))


def main():
    install_folder = Path.cwd()
    fill_folder = Path.cwd() / 'Filler'
    folder_filler(install_folder, fill_folder, 5, 4, 3)


if __name__ == '__main__':
    main()
