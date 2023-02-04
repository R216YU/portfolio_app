import random

from django.shortcuts import render, redirect

# Create your views here.

# HOME
def home_func(request):
    params = {
        "page_title": "HOME / TeamBalanceBot",
    }
    return render(request, "home.html", params)


# VALORANT
class ValorantPlayer(object):
    players = []
    
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.rating = VALORANT_RANK[rank]
        self.players.append(self)
    
    def __repr__(self):
        return f"{self.name} : {self.rank}"

VALORANT_RANK = {
    "radiant": 70,
    "immortal": 55,
    "ascendant": 45,
    "diamond": 40,
    "platinum": 35,
    "gold": 30,
    "silver": 20,
    "bronze": 15,
    "iron": 10, 
}
VALORANT_RANK_NAME = list(VALORANT_RANK.keys())


def valorant_func(request):
    params = {
        "page_title": "Valorant / TeamBalanceBot",
        "for_range": [i for i in range(1, 11)],
    }

    if request.method == "GET":
        return render(request, "valorant.html", params)
    
    else:
        ValorantPlayer.players = []
        # フォームからプレイヤーの情報を取得し、Playerインスタンスを作成
        for i in range(1, 11):
            player_name = request.POST[f"name-{i}"]
            player_rank = request.POST[f"rank-{i}"]
            player = ValorantPlayer(player_name, player_rank)
            player.rating += random.randint(-5, 5)
        # Playerインスタンスがまとめられたリストをランクレーティングでソート
        ValorantPlayer.players.sort(key=lambda player: player.rating)
        # ソートされた情報をもとにチーム分け
        TEAM_ATK = ValorantPlayer.players[::2]
        TEAM_DEF = ValorantPlayer.players[1::2]
        params["TEAM_ATK"] = TEAM_ATK
        params["TEAM_DEF"] = TEAM_DEF
        
        return render(request, "valorant.html", params)
        


# Overwatch2
class OverwatchPlayer(object):
    players = []
    
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.rating = OVERWATCH_RANK[rank]
        self.players.append(self)
    
    def __repr__(self):
        return f"{self.name} : {self.rank}"


OVERWATCH_RANK = {
    "grandmaster": 45,
    "master": 35,
    "diamond": 30,
    "platinum": 25,
    "gold": 20,
    "silver": 15,
    "bronze": 10, 
}

OVERWATCH_RANK_NAME = list(OVERWATCH_RANK.keys())


def overwatch_func(request):
    params = {
        "page_title": "Overwatch2 / TeamBalanceBot",
        "for_range": [i for i in range(1, 11)],
    }
    
    if request.method == "GET":
        return render(request, "overwatch.html", params)
    
    else:
        OverwatchPlayer.players = []
        # フォームからプレイヤーの情報を取得し、Playerインスタンスを作成
        for i in range(1, 11):
            player_name = request.POST[f"name-{i}"]
            player_rank = request.POST[f"rank-{i}"]
            player = OverwatchPlayer(player_name, player_rank)
            player.rating += random.randint(-5, 5)
        # Playerインスタンスがまとめられたリストをランクレーティングでソート
        OverwatchPlayer.players.sort(key=lambda player: player.rating)
        # ソートされた情報をもとにチーム分け
        TEAM_ATK = OverwatchPlayer.players[::2]
        TEAM_DEF = OverwatchPlayer.players[1::2]
        params["TEAM_ATK"] = TEAM_ATK
        params["TEAM_DEF"] = TEAM_DEF
        
        return render(request, "overwatch.html", params)