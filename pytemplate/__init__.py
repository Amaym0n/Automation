import os
import shutil


def copy_files() -> None:
    """
    Copy files and directories from the 'files' directory to the current directory.
    """
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
    target_dir = os.getcwd()
    shutil.copytree(source_dir, target_dir)
    return


copy_files()
