import tkinter as tk
from tkinter import messagebox
import random

RANDOM_EVENTS = [
    {"type": "reward", "name": "Skrzynia Porzucona", "description": "Znalazłeś skrzynię z 20 RFN!", "reward": {"rfn": 20}},
    {"type": "fight", "name": "Dziki Wilk", "description": "Zaatakował Cię Wilk Cienia! Tracisz 5 XP.", "penalty": {"xp": -5}},
    {"type": "trap", "name": "Runiczna Pułapka", "description": "Aktywowałeś pułapkę. Tracisz przedmiot.", "lose_item": True},
    {"type": "mystery", "name": "Stara Księga", "description": "Zdobywasz tajemną wiedzę. +5 XP", "reward": {"xp": 5}},
    {"type": "npc", "name": "Wędrowny Kupiec", "description": "Oferuje ci Miksturę Leczenia za darmo.", "reward": {"item": {"name": "Mikstura Leczenia", "level": 1}}}
]

def trigger_random_event(player_data):
    event = random.choice(RANDOM_EVENTS)
    result = event["description"]

    if "reward" in event:
        reward = event["reward"]
        if "rfn" in reward:
            player_data["rfn"] = player_data.get("rfn", 0) + reward["rfn"]
        if "xp" in reward:
            player_data["xp"] = player_data.get("xp", 0) + reward["xp"]
        if "item" in reward:
            if "inventory" not in player_data:
                player_data["inventory"] = []
            player_data["inventory"].append(reward["item"])
    if "penalty" in event:
        penalty = event["penalty"]
        if "xp" in penalty:
            player_data["xp"] = max(0, player_data.get("xp", 0) + penalty["xp"])
    if event.get("lose_item"):
        if player_data.get("inventory"):
            player_data["inventory"].pop()

    messagebox.showinfo(f"Event: {event['name']}", result)