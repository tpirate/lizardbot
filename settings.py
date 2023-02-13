from shutil import copyfile
import os
from stat import S_IREAD

# Replace the first parameter with your file name

def setsettings():
    try:
        copyfile('PersistedSettings.json', r'C:\Riot Games\League of Legends\Config\PersistedSettings.json')
        os.chmod(r'C:\Riot Games\League of Legends\Config\PersistedSettings.json', S_IREAD)
        return True
    except PermissionError:
        return True


if __name__ == "__main__":
    setsettings()