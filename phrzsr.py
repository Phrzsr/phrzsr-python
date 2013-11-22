from os.path import exists, abspath
import urllib
from random import choice

files_by_category = {
    "demotivational": "https://github.com/Phrzsr/phrzsr/raw/master/demotivational",
    "farewell": "https://github.com/Phrzsr/phrzsr/raw/master/farewell",
    "gratitude": "https://github.com/Phrzsr/phrzsr/raw/master/gratitude",
    "greeting": "https://github.com/Phrzsr/phrzsr/raw/master/greeting",
    "motivational": "https://github.com/Phrzsr/phrzsr/raw/master/motivational"
}

def phrzsr(category_or_url_or_path="", *substitutions):
    try:
        file = get_file(category_or_url_or_path)
    except:
        file = None
    
    if file is None:
        # Map category names to files.
        if category_or_url_or_path in files_by_category:
            file = get_file(files_by_category[category_or_url_or_path])
        # Use default file.
        else:
            file = get_file(files_by_category["greeting"])
    
    if file is None:
        return "Hi!"
    
    lines = file.readlines()
    if substitutions:
        substituted = None
        while substituted is None:
            attempt = choice(lines)
            try:
                substituted = attempt.format(*substitutions)
            except:
                pass
        return substituted
    
    return choice(lines)

def get_file(url_or_path):
    file = urllib.urlopen(url_or_path)
    if file is None and exists(url_or_path):
        file = urllib.urlopen("file:" + abspath(url_or_path))
    return file

if __name__ == "__main__":
    print(phrzsr())
