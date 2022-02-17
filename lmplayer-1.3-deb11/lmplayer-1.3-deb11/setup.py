# Here we imported the 'setup' module which allows us to install Python scripts to the local system beside performing some other tasks, you can find the documentation here: https://docs.python.org/2/distutils/apiref.html 
from distutils.core import setup 
import distutils.text_file
from pathlib import Path
from typing import List

def _parse_requirements(filename: str) -> List[str]:
    """Return requirements from requirements file."""
    # Ref: https://stackoverflow.com/a/42033122/
    return distutils.text_file.TextFile(filename=str(Path(__file__).with_name(filename))).readlines()
    
setup(name = "lmplayer", # Name of the program. 
      version = "1.3", # Version of the program. 
      description = "An easy-to-use mp3 player to show lyrics",
      author = "Mahdi Bahmani",
      author_email = "itstorage59@gmail.com",
      url = "https://www.itstorage.net",
      license='GPLv3',
      install_requires=_parse_requirements('requirements.txt'),
      scripts=['lmplayer'],
      data_files = [ ("lib/lmplayer", ["ui.glade"]),("lib/lmplayer", ["lmplayer.png"]),
                     ("share/applications", ["lmplayer1.3.desktop"])] 
)

