import os
import logging
import random
import sys

# Setup:
#  Needs ALttPEntranceRandomizer python script
#  Place SpriteRandomizer.py into ALttPER \data\ folder
#  Script will pull all *.sfc files in \data\gamefiles\
#  Script will pull a random *.zspr file from \data\sprites\ to patch into each *.sfc, choosing a random sprite each time (may result in duplicates)
# Usage:
#  python SpriteRandomizer.py
# Output:
#  Script will blindly write gamefiles to \data\ folder, overwriting files if they have the same filename
#  Script uses ERROR channel to print its messages as opposed to INFO which the main script uses

from argparse import Namespace

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from AdjusterMain import adjust

def get_filepaths(directory, filext = ""):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            appendFile = 0
            if filext != "":
                if filext in filename:
                    appendFile = 1
            else:
                appendFile = 1

            if appendFile == 1:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

def choose_random_sprite():
    sprites = get_filepaths("./sprites/",".zspr")
    return random.choice(sprites)

def choose_random_gamefile():
    gamefiles = get_filepaths("./gamefiles/",".sfc")
    return random.choice(gamefiles)

logging.basicConfig(format='%(message)s', level=logging.ERROR)
logger = logging.getLogger('')

gamefiles = get_filepaths("./gamefiles/",".sfc")

i = 0

for gamefile in gamefiles:
    args = Namespace(
      sprite = choose_random_sprite(),
      rom = gamefile,
      heartbeep = "normal",
      heartcolor = "red",
      quickswap = None,
      fastmenu = "off",
      disablemusic = None
    )

    i += 1
    logger.error("Patching ROM #" + str(i))
    adjust(args)
