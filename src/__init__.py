from dataclasses import dataclass
from permissions import Checks
from requests import HTTPError
import requests
import logging


@dataclass
class Profile:
    color: str
    emoji: str
    hasRecoveryCode: bool
    id: int
    mfaEnabled: bool
    name: str
    shape: str


class API:
    ENDPOINT = "https://payphonetag.com/api/"
    PLAYER_SNAPSHOT = ENDPOINT + "player-snapshot"
    IDENTITY = ENDPOINT + "identity"
    PLAYER_STATS = ENDPOINT + "player-stats"
    BADGES = ENDPOINT + "badges"
    BADGES_SUMMARY = ENDPOINT + "badges/summary"
    GAME_STATS = ENDPOINT + "game-stats"
    PREFERENCES = ENDPOINT + "notification-prefs"

    # Push Notifications
    PUSH = ENDPOINT + "push/"
    SUBSCRIBE = PUSH + "subscribe"
    UNSUBSCRIBE = PUSH + "unsubscribe"
    VAPID = PUSH + "vapid-key"

    # Account
    



class Client:
    def __init__(self):
        self.ratelimits: dict[str: bool] = {
            "authentication": False
        }
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Python Payphonetag Client"})
        self.logged_in: bool = False
        self.pin: int = None
        self.profile: Profile = None

    def login(self, pin: int, relog: bool = False) -> bool:
        if self.logged_in and relog == False:
            raise Exception("Already logged in, pass relog = True and retry.")

        if self.ratelimits["authentication"] == True:
            return False

        try:
            response = self.session.post(API.IDENTITY, {"pin": pin})
            response.raise_for_status()
        except HTTPError as error:
            logging.exception(error)
            if response.status_code == 429:
                self.ratelimits["authentication"] = True
            return False

        except Exception as error:
            logging.exception(error)
            return False

        response_data: dict = response.json()
        self.profile = Profile(**response_data)
        self.pin = pin
        self.logged_in = True
        return True

    def get_payphone(self, payphone_id):
        pass

    def get_payphones(self):
        pass

    def get_emojis(self):
        pass

    def get_badges(self):
        pass

    def get_callsigns(self):
        pass

    def get_leaderboard(self):
        pass

    def get_ranks(self):
        pass

    def get_player_stats(self):
        pass

    def get_player_activity(self):
        pass

    def get_player_snapshot(self):
        pass

    def get_topology(self):
        pass

    def get_territory(self):
        pass

    def get_cell(self):
        pass

    def get_cell_leaderboard(self):
        pass

    def get_past_captures(self, player_id: int):
        pass

    def get_players(self):
        pass

    def get_game_stats(self):
        pass

    # PUSH NOTIFICATIONS
    def subscribe_push(self):
        pass  # POST

    def unsubscribe_push(self):
        pass  # POST

    def get_vapid_key(self):
        pass  # GET

    def save_notification_preferences(self):
        pass  # POST
