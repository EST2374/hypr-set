import re
from dataclasses import dataclass


@dataclass
class SettingConfig:
    setting: str
    pattern: str
    data_type: type


SETTINGS_MAP = {"gaps_in": SettingConfig("gaps_in", r"^\s*gaps_in\s*=.*", int)}


config = SETTINGS_MAP.get("gaps_in")
