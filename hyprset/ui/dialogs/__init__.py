from .autostart import AddProgramDialog, AddScriptDialog
from .base import BaseDialog
from .environment import AddEnvDialog, EditLineDialog
from .hypridle import EditHypridle, EditHypridleGeneral
from .hyprpaper import EditHyprpaper
from .hyprsunset import EditHyprsunset
from .keybinding import EditKeybindingDialog
from .system import InstallHyprStuff, Update
from .wifi import Connect_to_Wifi
from .window_rule import EditWindowRule

__all__ = [
    "BaseDialog",
    "AddProgramDialog",
    "AddScriptDialog",
    "AddEnvDialog",
    "EditLineDialog",
    "Connect_to_Wifi",
    "Update",
    "InstallHyprStuff",
    "EditKeybindingDialog",
    "EditWindowRule",
    "EditHyprpaper",
    "EditHyprsunset",
    "EditHypridle",
    "EditHypridleGeneral",
]
