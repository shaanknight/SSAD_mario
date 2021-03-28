The game "little mario" is a basic version of mario game that has certain features of the original game .
It is built using python3.

command for launching the game : 
```sh
python3 main.py
```

Controls :

- enter : start the game
- q : quit
- a : left horizontal move
- d : right horizontal move
- w : rises straight up to a limited height, it takes care of sidewise movement while on upward flight
- s : advanced jump , a projectile motion 

Features:

- The game is divided into 2 levels.
- Bricks, Pillars and some opponents(Frown Man, Alien, Monkey King, cactus and few nasty creatures) appear throughout game.
   The opponents are basically static enemies.
- Clouds and Trees appear in the background and have no roleplay in the game.
- In level 1 just opponents try to stop you.
- In level 2 an enemy appears in the way to home which moves to and fro about its position besides the opponents.
- The opponents and enemy can only be killed if the mario somehow lands on them while advanced jumps.
- The mario has been provided with few lives and 8 advanced jumps.
- You get a score which is a function of remaining advanced jumps and lives . 
- Each life is lost as you touch any opponent or enemy in any other situation except the landing of mario.

Tree structure of folder :
.
├── background.py
├── board.py
├── checkcell.py
├── config.py
├── drawnext.py
├── enemy.py
├── main.py
├── neighbours.py
├── opponents.py
├── person.py
├── README.md
└── theme.wav

0 directories, 12 files
