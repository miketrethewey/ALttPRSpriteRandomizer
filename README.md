# ALttPRSpriteRandomizer
Script for use with [ALttPEntranceRandomizer](http://github.com/KevinCathcart/ALttPEntranceRandomizer) (*"ALttPER"*) to add random sprites to game files

## Setup
* Needs [python](https://www.python.org/downloads/)
* Needs [*ALttPER*](http://github.com/KevinCathcart/ALttPEntranceRandomizer) python script
* Place `SpriteRandomizer.py` into *ALttPER* `\data\` folder
* Script will pull all `*.sfc` files in `\data\gamefiles\`
* Script will pull a random `*.zspr` file from `\data\sprites\` to patch into each `*.sfc`, choosing a random sprite each time (may result in duplicates)

## Usage
* `python SpriteRandomizer.py`

## Output:
* Script will blindly write gamefiles to `\data\` folder, overwriting files if they have the same filename
* Script uses ERROR channel to print its messages as opposed to INFO which the main script uses
