import os

input = input("Give path")

my_path = input


class PathHandler:
    def __init__(self) -> None:
        pass

    def _remove_quotes(self, path):
        """Removes reduntant quotation marks"""
        return path.replace('"', "")

    def check_dir_path(self, path):
        """Checks if directory path is correct"""
        dir_path = self._remove_quotes(path)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            return dir_path
        else:
            print("Given path does not exist or is not a directory.")

    def check_file_path(self, path):
        """Checks if file path is correct"""
        file_path = self._remove_quotes(path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return file_path
        else:
            print("Given path does not exist or is not a file.")


print(my_path)
