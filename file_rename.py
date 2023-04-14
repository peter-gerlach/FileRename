import os
import logging as log

ROOTPATH = "/Path/To/Root"


class directory:
    def __init__(self, path: str, filenames: list[str]):
        self.path = path
        self.filenames = filenames

    def __str__(self) -> str:
        return f"Path: {self.path} | Files: {len(self.filenames)}"


def getAllDirectories(path: str) -> list[directory]:
    directories = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        directories.append(directory(dirpath, filenames))
    return directories


def renameFiles(dir: directory):
    log.info(f"Working on directory {dir}")

    relative_path = dir.path.replace(ROOTPATH, "").strip("/")
    folders = relative_path.split("/")

    base_name = '-'.join(folders)
    for i, file in enumerate(dir.filenames):

        file_ending = file.split(".")[-1]
        old_name = os.path.join(dir.path, file)
        new_name = os.path.join(dir.path, f"{base_name}_{i}.{file_ending}")
        log.info(f"{i} : {old_name}")
        os.rename(old_name, new_name)


if __name__ == "__main__":
    log.basicConfig(filename="rename.log", level=log.DEBUG,
                    format='%(levelname)s:%(message)s')

    log.info("====================================")
    log.info("Starting new renaming!")
    log.info("====================================")

    directories = getAllDirectories(ROOTPATH)
    for dir in directories:
        renameFiles(dir)
