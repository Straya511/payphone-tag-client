from requests import HTTPError
from dataclasses import dataclass
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
    IDENTITY = ENDPOINT + "indentiy"


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
