import random

class Player(object):
    players = []
    
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.rating = VALORANT_RANK[rank] + random.randint(-5, 5)
        self.players.append(self)
    
    def __repr__(self):
        return f"{self.name} : {self.rank}"

VALORANT_RANK = {
    "radiant": 90,
    "immortal": 70,
    "ascendant": 55,
    "diamond": 45,
    "platinum": 35,
    "gold": 30,
    "silver": 20,
    "bronze": 15,
    "iron": 10, 
}
VALORANT_RANK_NAME = list(VALORANT_RANK.keys())

def valorant_func():
    Player.players = []
    for i in range(1, 11):
        player_name = i
        player_rank = random.choice(VALORANT_RANK_NAME)
        Player(player_name, player_rank)
    Player.players.sort(key=lambda x: VALORANT_RANK[x.rank])
    TEAM_ATK = Player.players[::2]
    TEAM_DEF = Player.players[1::2]
    print(f"""
          TEAM_ATK : {TEAM_ATK} 
          TEAM_DEF : {TEAM_DEF}
          """)
    
    params = {
        "TEAM_ATK": TEAM_ATK,
        "TEAM_DEF": TEAM_DEF,
    }
valorant_func()