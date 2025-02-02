"""Classes for all tiers of effectivity/productivity/quality/speed modules."""
import json
import os

# Load data from JSON file
# See the JSON file specified by the path below for format
DATA_PATH = os.path.join("data", "modules.json")
MODULE_LIST: list[dict] = []  # List of all possible modules
MODULE_DICT = {}  # Dict of modules, with key being their name and value same as in MODULE_LIST
try:
    with open(DATA_PATH, "r", encoding="utf8") as _file:
        MODULE_LIST.extend(json.load(_file))
    MODULE_DICT = {module["name"]: module for module in MODULE_LIST}
except FileNotFoundError:
    raise FileNotFoundError(f"Could not open module JSON data file at {DATA_PATH}")


class Module():
    """Base class for all tiers and types of modules."""

    energy_consumption = 0.
    pollution = 0.
    productivity = 0.
    quality = 0.
    speed = 0.


# Efficiency =======================================================================================
class Efficiency1(Module):
    """Normal Efficiency 1 module."""

    energy_consumption = MODULE_DICT["Efficiency module"]["energy_consumption"][0]
    pollution = MODULE_DICT["Efficiency module"]["pollution"][0]
    productivity = MODULE_DICT["Efficiency module"]["productivity"][0]
    quality = MODULE_DICT["Efficiency module"]["quality"][0]
    speed = MODULE_DICT["Efficiency module"]["speed"][0]


class Efficiency2(Module):
    """Normal Efficiency 2 module."""

    energy_consumption = MODULE_DICT["Efficiency module 2"]["energy_consumption"][0]
    pollution = MODULE_DICT["Efficiency module 2"]["pollution"][0]
    productivity = MODULE_DICT["Efficiency module 2"]["productivity"][0]
    quality = MODULE_DICT["Efficiency module 2"]["quality"][0]
    speed = MODULE_DICT["Efficiency module 2"]["speed"][0]


class Efficiency3(Module):
    """Normal Efficiency 3 module."""

    energy_consumption = MODULE_DICT["Efficiency module 3"]["energy_consumption"][0]
    pollution = MODULE_DICT["Efficiency module 3"]["pollution"][0]
    productivity = MODULE_DICT["Efficiency module 3"]["productivity"][0]
    quality = MODULE_DICT["Efficiency module 3"]["quality"][0]
    speed = MODULE_DICT["Efficiency module 3"]["speed"][0]


class Efficiency1Uncommon(Module):
    """Uncommon Efficiency 1 module."""

    energy_consumption = MODULE_DICT["Efficiency module"]["energy_consumption"][1]
    pollution = MODULE_DICT["Efficiency module"]["pollution"][1]
    productivity = MODULE_DICT["Efficiency module"]["productivity"][1]
    quality = MODULE_DICT["Efficiency module"]["quality"][1]
    speed = MODULE_DICT["Efficiency module"]["speed"][1]


class Efficiency2Uncommon(Module):
    """Uncommon Efficiency 2 module."""

    energy_consumption = MODULE_DICT["Efficiency module 2"]["energy_consumption"][1]
    pollution = MODULE_DICT["Efficiency module 2"]["pollution"][1]
    productivity = MODULE_DICT["Efficiency module 2"]["productivity"][1]
    quality = MODULE_DICT["Efficiency module 2"]["quality"][1]
    speed = MODULE_DICT["Efficiency module 2"]["speed"][1]


class Efficiency3Uncommon(Module):
    """Uncommon Efficiency 3 module."""

    energy_consumption = MODULE_DICT["Efficiency module 3"]["energy_consumption"][1]
    pollution = MODULE_DICT["Efficiency module 3"]["pollution"][1]
    productivity = MODULE_DICT["Efficiency module 3"]["productivity"][1]
    quality = MODULE_DICT["Efficiency module 3"]["quality"][1]
    speed = MODULE_DICT["Efficiency module 3"]["speed"][1]


class Efficiency1Rare(Module):
    """Rare Efficiency 1 module."""

    energy_consumption = MODULE_DICT["Efficiency module"]["energy_consumption"][2]
    pollution = MODULE_DICT["Efficiency module"]["pollution"][2]
    productivity = MODULE_DICT["Efficiency module"]["productivity"][2]
    quality = MODULE_DICT["Efficiency module"]["quality"][2]
    speed = MODULE_DICT["Efficiency module"]["speed"][2]


class Efficiency2Rare(Module):
    """Rare Efficiency 2 module."""

    energy_consumption = MODULE_DICT["Efficiency module 2"]["energy_consumption"][2]
    pollution = MODULE_DICT["Efficiency module 2"]["pollution"][2]
    productivity = MODULE_DICT["Efficiency module 2"]["productivity"][2]
    quality = MODULE_DICT["Efficiency module 2"]["quality"][2]
    speed = MODULE_DICT["Efficiency module 2"]["speed"][2]


class Efficiency3Rare(Module):
    """Rare Efficiency 3 module."""

    energy_consumption = MODULE_DICT["Efficiency module 3"]["energy_consumption"][2]
    pollution = MODULE_DICT["Efficiency module 3"]["pollution"][2]
    productivity = MODULE_DICT["Efficiency module 3"]["productivity"][2]
    quality = MODULE_DICT["Efficiency module 3"]["quality"][2]
    speed = MODULE_DICT["Efficiency module 3"]["speed"][2]


class Efficiency1Epic(Module):
    """Epic Efficiency 1 module."""

    energy_consumption = MODULE_DICT["Efficiency module"]["energy_consumption"][3]
    pollution = MODULE_DICT["Efficiency module"]["pollution"][3]
    productivity = MODULE_DICT["Efficiency module"]["productivity"][3]
    quality = MODULE_DICT["Efficiency module"]["quality"][3]
    speed = MODULE_DICT["Efficiency module"]["speed"][3]


class Efficiency2Epic(Module):
    """Epic Efficiency 2 module."""

    energy_consumption = MODULE_DICT["Efficiency module 2"]["energy_consumption"][3]
    pollution = MODULE_DICT["Efficiency module 2"]["pollution"][3]
    productivity = MODULE_DICT["Efficiency module 2"]["productivity"][3]
    quality = MODULE_DICT["Efficiency module 2"]["quality"][3]
    speed = MODULE_DICT["Efficiency module 2"]["speed"][3]


class Efficiency3Epic(Module):
    """Epic Efficiency 3 module."""

    energy_consumption = MODULE_DICT["Efficiency module 3"]["energy_consumption"][3]
    pollution = MODULE_DICT["Efficiency module 3"]["pollution"][3]
    productivity = MODULE_DICT["Efficiency module 3"]["productivity"][3]
    quality = MODULE_DICT["Efficiency module 3"]["quality"][3]
    speed = MODULE_DICT["Efficiency module 3"]["speed"][3]


class Efficiency1Legendary(Module):
    """Legendary Efficiency 1 module."""

    energy_consumption = MODULE_DICT["Efficiency module"]["energy_consumption"][4]
    pollution = MODULE_DICT["Efficiency module"]["pollution"][4]
    productivity = MODULE_DICT["Efficiency module"]["productivity"][4]
    quality = MODULE_DICT["Efficiency module"]["quality"][4]
    speed = MODULE_DICT["Efficiency module"]["speed"][4]


class Efficiency2Legendary(Module):
    """Legendary Efficiency 2 module."""

    energy_consumption = MODULE_DICT["Efficiency module 2"]["energy_consumption"][4]
    pollution = MODULE_DICT["Efficiency module 2"]["pollution"][4]
    productivity = MODULE_DICT["Efficiency module 2"]["productivity"][4]
    quality = MODULE_DICT["Efficiency module 2"]["quality"][4]
    speed = MODULE_DICT["Efficiency module 2"]["speed"][4]


class Efficiency3Legendary(Module):
    """Legendary Efficiency 3 module."""

    energy_consumption = MODULE_DICT["Efficiency module 3"]["energy_consumption"][4]
    pollution = MODULE_DICT["Efficiency module 3"]["pollution"][4]
    productivity = MODULE_DICT["Efficiency module 3"]["productivity"][4]
    quality = MODULE_DICT["Efficiency module 3"]["quality"][4]
    speed = MODULE_DICT["Efficiency module 3"]["speed"][4]


# Productivity =====================================================================================
class Productivity1(Module):
    """Normal Productivity 1 module."""

    energy_consumption = MODULE_DICT["Productivity module"]["energy_consumption"][0]
    pollution = MODULE_DICT["Productivity module"]["pollution"][0]
    productivity = MODULE_DICT["Productivity module"]["productivity"][0]
    quality = MODULE_DICT["Productivity module"]["quality"][0]
    speed = MODULE_DICT["Productivity module"]["speed"][0]


class Productivity2(Module):
    """Normal Productivity 2 module."""

    energy_consumption = MODULE_DICT["Productivity module 2"]["energy_consumption"][0]
    pollution = MODULE_DICT["Productivity module 2"]["pollution"][0]
    productivity = MODULE_DICT["Productivity module 2"]["productivity"][0]
    quality = MODULE_DICT["Productivity module 2"]["quality"][0]
    speed = MODULE_DICT["Productivity module 2"]["speed"][0]


class Productivity3(Module):
    """Normal Productivity 3 module."""

    energy_consumption = MODULE_DICT["Productivity module 3"]["energy_consumption"][0]
    pollution = MODULE_DICT["Productivity module 3"]["pollution"][0]
    productivity = MODULE_DICT["Productivity module 3"]["productivity"][0]
    quality = MODULE_DICT["Productivity module 3"]["quality"][0]
    speed = MODULE_DICT["Productivity module 3"]["speed"][0]


class Productivity1Uncommon(Module):
    """Uncommon Productivity 1 module."""

    energy_consumption = MODULE_DICT["Productivity module"]["energy_consumption"][1]
    pollution = MODULE_DICT["Productivity module"]["pollution"][1]
    productivity = MODULE_DICT["Productivity module"]["productivity"][1]
    quality = MODULE_DICT["Productivity module"]["quality"][1]
    speed = MODULE_DICT["Productivity module"]["speed"][1]


class Productivity2Uncommon(Module):
    """Uncommon Productivity 2 module."""

    energy_consumption = MODULE_DICT["Productivity module 2"]["energy_consumption"][1]
    pollution = MODULE_DICT["Productivity module 2"]["pollution"][1]
    productivity = MODULE_DICT["Productivity module 2"]["productivity"][1]
    quality = MODULE_DICT["Productivity module 2"]["quality"][1]
    speed = MODULE_DICT["Productivity module 2"]["speed"][1]


class Productivity3Uncommon(Module):
    """Uncommon Productivity 3 module."""

    energy_consumption = MODULE_DICT["Productivity module 3"]["energy_consumption"][1]
    pollution = MODULE_DICT["Productivity module 3"]["pollution"][1]
    productivity = MODULE_DICT["Productivity module 3"]["productivity"][1]
    quality = MODULE_DICT["Productivity module 3"]["quality"][1]
    speed = MODULE_DICT["Productivity module 3"]["speed"][1]


class Productivity1Rare(Module):
    """Rare Productivity 1 module."""

    energy_consumption = MODULE_DICT["Productivity module"]["energy_consumption"][2]
    pollution = MODULE_DICT["Productivity module"]["pollution"][2]
    productivity = MODULE_DICT["Productivity module"]["productivity"][2]
    quality = MODULE_DICT["Productivity module"]["quality"][2]
    speed = MODULE_DICT["Productivity module"]["speed"][2]


class Productivity2Rare(Module):
    """Rare Productivity 2 module."""

    energy_consumption = MODULE_DICT["Productivity module 2"]["energy_consumption"][2]
    pollution = MODULE_DICT["Productivity module 2"]["pollution"][2]
    productivity = MODULE_DICT["Productivity module 2"]["productivity"][2]
    quality = MODULE_DICT["Productivity module 2"]["quality"][2]
    speed = MODULE_DICT["Productivity module 2"]["speed"][2]


class Productivity3Rare(Module):
    """Rare Productivity 3 module."""

    energy_consumption = MODULE_DICT["Productivity module 3"]["energy_consumption"][2]
    pollution = MODULE_DICT["Productivity module 3"]["pollution"][2]
    productivity = MODULE_DICT["Productivity module 3"]["productivity"][2]
    quality = MODULE_DICT["Productivity module 3"]["quality"][2]
    speed = MODULE_DICT["Productivity module 3"]["speed"][2]


class Productivity1Epic(Module):
    """Epic Productivity 1 module."""

    energy_consumption = MODULE_DICT["Productivity module"]["energy_consumption"][3]
    pollution = MODULE_DICT["Productivity module"]["pollution"][3]
    productivity = MODULE_DICT["Productivity module"]["productivity"][3]
    quality = MODULE_DICT["Productivity module"]["quality"][3]
    speed = MODULE_DICT["Productivity module"]["speed"][3]


class Productivity2Epic(Module):
    """Epic Productivity 2 module."""

    energy_consumption = MODULE_DICT["Productivity module 2"]["energy_consumption"][3]
    pollution = MODULE_DICT["Productivity module 2"]["pollution"][3]
    productivity = MODULE_DICT["Productivity module 2"]["productivity"][3]
    quality = MODULE_DICT["Productivity module 2"]["quality"][3]
    speed = MODULE_DICT["Productivity module 2"]["speed"][3]


class Productivity3Epic(Module):
    """Epic Productivity 3 module."""

    energy_consumption = MODULE_DICT["Productivity module 3"]["energy_consumption"][3]
    pollution = MODULE_DICT["Productivity module 3"]["pollution"][3]
    productivity = MODULE_DICT["Productivity module 3"]["productivity"][3]
    quality = MODULE_DICT["Productivity module 3"]["quality"][3]
    speed = MODULE_DICT["Productivity module 3"]["speed"][3]


class Productivity1Legendary(Module):
    """Legendary Productivity 1 module."""

    energy_consumption = MODULE_DICT["Productivity module"]["energy_consumption"][4]
    pollution = MODULE_DICT["Productivity module"]["pollution"][4]
    productivity = MODULE_DICT["Productivity module"]["productivity"][4]
    quality = MODULE_DICT["Productivity module"]["quality"][4]
    speed = MODULE_DICT["Productivity module"]["speed"][4]


class Productivity2Legendary(Module):
    """Legendary Productivity 2 module."""

    energy_consumption = MODULE_DICT["Productivity module 2"]["energy_consumption"][4]
    pollution = MODULE_DICT["Productivity module 2"]["pollution"][4]
    productivity = MODULE_DICT["Productivity module 2"]["productivity"][4]
    quality = MODULE_DICT["Productivity module 2"]["quality"][4]
    speed = MODULE_DICT["Productivity module 2"]["speed"][4]


class Productivity3Legendary(Module):
    """Legendary Productivity 3 module."""

    energy_consumption = MODULE_DICT["Productivity module 3"]["energy_consumption"][4]
    pollution = MODULE_DICT["Productivity module 3"]["pollution"][4]
    productivity = MODULE_DICT["Productivity module 3"]["productivity"][4]
    quality = MODULE_DICT["Productivity module 3"]["quality"][4]
    speed = MODULE_DICT["Productivity module 3"]["speed"][4]


# Quality ==========================================================================================
class Quality1(Module):
    """Normal Quality 1 module."""

    energy_consumption = MODULE_DICT["Quality module"]["energy_consumption"][0]
    pollution = MODULE_DICT["Quality module"]["pollution"][0]
    productivity = MODULE_DICT["Quality module"]["productivity"][0]
    quality = MODULE_DICT["Quality module"]["quality"][0]
    speed = MODULE_DICT["Quality module"]["speed"][0]


class Quality2(Module):
    """Normal Quality 2 module."""

    energy_consumption = MODULE_DICT["Quality module 2"]["energy_consumption"][0]
    pollution = MODULE_DICT["Quality module 2"]["pollution"][0]
    productivity = MODULE_DICT["Quality module 2"]["productivity"][0]
    quality = MODULE_DICT["Quality module 2"]["quality"][0]
    speed = MODULE_DICT["Quality module 2"]["speed"][0]


class Quality3(Module):
    """Normal Quality 3 module."""

    energy_consumption = MODULE_DICT["Quality module 3"]["energy_consumption"][0]
    pollution = MODULE_DICT["Quality module 3"]["pollution"][0]
    productivity = MODULE_DICT["Quality module 3"]["productivity"][0]
    quality = MODULE_DICT["Quality module 3"]["quality"][0]
    speed = MODULE_DICT["Quality module 3"]["speed"][0]


class Quality1Uncommon(Module):
    """Uncommon Quality 1 module."""

    energy_consumption = MODULE_DICT["Quality module"]["energy_consumption"][1]
    pollution = MODULE_DICT["Quality module"]["pollution"][1]
    productivity = MODULE_DICT["Quality module"]["productivity"][1]
    quality = MODULE_DICT["Quality module"]["quality"][1]
    speed = MODULE_DICT["Quality module"]["speed"][1]


class Quality2Uncommon(Module):
    """Uncommon Quality 2 module."""

    energy_consumption = MODULE_DICT["Quality module 2"]["energy_consumption"][1]
    pollution = MODULE_DICT["Quality module 2"]["pollution"][1]
    productivity = MODULE_DICT["Quality module 2"]["productivity"][1]
    quality = MODULE_DICT["Quality module 2"]["quality"][1]
    speed = MODULE_DICT["Quality module 2"]["speed"][1]


class Quality3Uncommon(Module):
    """Uncommon Quality 3 module."""

    energy_consumption = MODULE_DICT["Quality module 3"]["energy_consumption"][1]
    pollution = MODULE_DICT["Quality module 3"]["pollution"][1]
    productivity = MODULE_DICT["Quality module 3"]["productivity"][1]
    quality = MODULE_DICT["Quality module 3"]["quality"][1]
    speed = MODULE_DICT["Quality module 3"]["speed"][1]


class Quality1Rare(Module):
    """Rare Quality 1 module."""

    energy_consumption = MODULE_DICT["Quality module"]["energy_consumption"][2]
    pollution = MODULE_DICT["Quality module"]["pollution"][2]
    productivity = MODULE_DICT["Quality module"]["productivity"][2]
    quality = MODULE_DICT["Quality module"]["quality"][2]
    speed = MODULE_DICT["Quality module"]["speed"][2]


class Quality2Rare(Module):
    """Rare Quality 2 module."""

    energy_consumption = MODULE_DICT["Quality module 2"]["energy_consumption"][2]
    pollution = MODULE_DICT["Quality module 2"]["pollution"][2]
    productivity = MODULE_DICT["Quality module 2"]["productivity"][2]
    quality = MODULE_DICT["Quality module 2"]["quality"][2]
    speed = MODULE_DICT["Quality module 2"]["speed"][2]


class Quality3Rare(Module):
    """Rare Quality 3 module."""

    energy_consumption = MODULE_DICT["Quality module 3"]["energy_consumption"][2]
    pollution = MODULE_DICT["Quality module 3"]["pollution"][2]
    productivity = MODULE_DICT["Quality module 3"]["productivity"][2]
    quality = MODULE_DICT["Quality module 3"]["quality"][2]
    speed = MODULE_DICT["Quality module 3"]["speed"][2]


class Quality1Epic(Module):
    """Epic Quality 1 module."""

    energy_consumption = MODULE_DICT["Quality module"]["energy_consumption"][3]
    pollution = MODULE_DICT["Quality module"]["pollution"][3]
    productivity = MODULE_DICT["Quality module"]["productivity"][3]
    quality = MODULE_DICT["Quality module"]["quality"][3]
    speed = MODULE_DICT["Quality module"]["speed"][3]


class Quality2Epic(Module):
    """Epic Quality 2 module."""

    energy_consumption = MODULE_DICT["Quality module 2"]["energy_consumption"][3]
    pollution = MODULE_DICT["Quality module 2"]["pollution"][3]
    productivity = MODULE_DICT["Quality module 2"]["productivity"][3]
    quality = MODULE_DICT["Quality module 2"]["quality"][3]
    speed = MODULE_DICT["Quality module 2"]["speed"][3]


class Quality3Epic(Module):
    """Epic Quality 3 module."""

    energy_consumption = MODULE_DICT["Quality module 3"]["energy_consumption"][3]
    pollution = MODULE_DICT["Quality module 3"]["pollution"][3]
    productivity = MODULE_DICT["Quality module 3"]["productivity"][3]
    quality = MODULE_DICT["Quality module 3"]["quality"][3]
    speed = MODULE_DICT["Quality module 3"]["speed"][3]


class Quality1Legendary(Module):
    """Legendary Quality 1 module."""

    energy_consumption = MODULE_DICT["Quality module"]["energy_consumption"][4]
    pollution = MODULE_DICT["Quality module"]["pollution"][4]
    productivity = MODULE_DICT["Quality module"]["productivity"][4]
    quality = MODULE_DICT["Quality module"]["quality"][4]
    speed = MODULE_DICT["Quality module"]["speed"][4]


class Quality2Legendary(Module):
    """Legendary Quality 2 module."""

    energy_consumption = MODULE_DICT["Quality module 2"]["energy_consumption"][4]
    pollution = MODULE_DICT["Quality module 2"]["pollution"][4]
    productivity = MODULE_DICT["Quality module 2"]["productivity"][4]
    quality = MODULE_DICT["Quality module 2"]["quality"][4]
    speed = MODULE_DICT["Quality module 2"]["speed"][4]


class Quality3Legendary(Module):
    """Legendary Quality 3 module."""

    energy_consumption = MODULE_DICT["Quality module 3"]["energy_consumption"][4]
    pollution = MODULE_DICT["Quality module 3"]["pollution"][4]
    productivity = MODULE_DICT["Quality module 3"]["productivity"][4]
    quality = MODULE_DICT["Quality module 3"]["quality"][4]
    speed = MODULE_DICT["Quality module 3"]["speed"][4]


# Speed ============================================================================================
class Speed1(Module):
    """Normal Speed 1 module."""

    energy_consumption = MODULE_DICT["Speed module"]["energy_consumption"][0]
    pollution = MODULE_DICT["Speed module"]["pollution"][0]
    productivity = MODULE_DICT["Speed module"]["productivity"][0]
    quality = MODULE_DICT["Speed module"]["quality"][0]
    speed = MODULE_DICT["Speed module"]["speed"][0]


class Speed2(Module):
    """Normal Speed 2 module."""

    energy_consumption = MODULE_DICT["Speed module 2"]["energy_consumption"][0]
    pollution = MODULE_DICT["Speed module 2"]["pollution"][0]
    productivity = MODULE_DICT["Speed module 2"]["productivity"][0]
    quality = MODULE_DICT["Speed module 2"]["quality"][0]
    speed = MODULE_DICT["Speed module 2"]["speed"][0]


class Speed3(Module):
    """Normal Speed 3 module."""

    energy_consumption = MODULE_DICT["Speed module 3"]["energy_consumption"][0]
    pollution = MODULE_DICT["Speed module 3"]["pollution"][0]
    productivity = MODULE_DICT["Speed module 3"]["productivity"][0]
    quality = MODULE_DICT["Speed module 3"]["quality"][0]
    speed = MODULE_DICT["Speed module 3"]["speed"][0]


class Speed1Uncommon(Module):
    """Uncommon Speed 1 module."""

    energy_consumption = MODULE_DICT["Speed module"]["energy_consumption"][1]
    pollution = MODULE_DICT["Speed module"]["pollution"][1]
    productivity = MODULE_DICT["Speed module"]["productivity"][1]
    quality = MODULE_DICT["Speed module"]["quality"][1]
    speed = MODULE_DICT["Speed module"]["speed"][1]


class Speed2Uncommon(Module):
    """Uncommon Speed 2 module."""

    energy_consumption = MODULE_DICT["Speed module 2"]["energy_consumption"][1]
    pollution = MODULE_DICT["Speed module 2"]["pollution"][1]
    productivity = MODULE_DICT["Speed module 2"]["productivity"][1]
    quality = MODULE_DICT["Speed module 2"]["quality"][1]
    speed = MODULE_DICT["Speed module 2"]["speed"][1]


class Speed3Uncommon(Module):
    """Uncommon Speed 3 module."""

    energy_consumption = MODULE_DICT["Speed module 3"]["energy_consumption"][1]
    pollution = MODULE_DICT["Speed module 3"]["pollution"][1]
    productivity = MODULE_DICT["Speed module 3"]["productivity"][1]
    quality = MODULE_DICT["Speed module 3"]["quality"][1]
    speed = MODULE_DICT["Speed module 3"]["speed"][1]


class Speed1Rare(Module):
    """Rare Speed 1 module."""

    energy_consumption = MODULE_DICT["Speed module"]["energy_consumption"][2]
    pollution = MODULE_DICT["Speed module"]["pollution"][2]
    productivity = MODULE_DICT["Speed module"]["productivity"][2]
    quality = MODULE_DICT["Speed module"]["quality"][2]
    speed = MODULE_DICT["Speed module"]["speed"][2]


class Speed2Rare(Module):
    """Rare Speed 2 module."""

    energy_consumption = MODULE_DICT["Speed module 2"]["energy_consumption"][2]
    pollution = MODULE_DICT["Speed module 2"]["pollution"][2]
    productivity = MODULE_DICT["Speed module 2"]["productivity"][2]
    quality = MODULE_DICT["Speed module 2"]["quality"][2]
    speed = MODULE_DICT["Speed module 2"]["speed"][2]


class Speed3Rare(Module):
    """Rare Speed 3 module."""

    energy_consumption = MODULE_DICT["Speed module 3"]["energy_consumption"][2]
    pollution = MODULE_DICT["Speed module 3"]["pollution"][2]
    productivity = MODULE_DICT["Speed module 3"]["productivity"][2]
    quality = MODULE_DICT["Speed module 3"]["quality"][2]
    speed = MODULE_DICT["Speed module 3"]["speed"][2]


class Speed1Epic(Module):
    """Epic Speed 1 module."""

    energy_consumption = MODULE_DICT["Speed module"]["energy_consumption"][3]
    pollution = MODULE_DICT["Speed module"]["pollution"][3]
    productivity = MODULE_DICT["Speed module"]["productivity"][3]
    quality = MODULE_DICT["Speed module"]["quality"][3]
    speed = MODULE_DICT["Speed module"]["speed"][3]


class Speed2Epic(Module):
    """Epic Speed 2 module."""

    energy_consumption = MODULE_DICT["Speed module 2"]["energy_consumption"][3]
    pollution = MODULE_DICT["Speed module 2"]["pollution"][3]
    productivity = MODULE_DICT["Speed module 2"]["productivity"][3]
    quality = MODULE_DICT["Speed module 2"]["quality"][3]
    speed = MODULE_DICT["Speed module 2"]["speed"][3]


class Speed3Epic(Module):
    """Epic Speed 3 module."""

    energy_consumption = MODULE_DICT["Speed module 3"]["energy_consumption"][3]
    pollution = MODULE_DICT["Speed module 3"]["pollution"][3]
    productivity = MODULE_DICT["Speed module 3"]["productivity"][3]
    quality = MODULE_DICT["Speed module 3"]["quality"][3]
    speed = MODULE_DICT["Speed module 3"]["speed"][3]


class Speed1Legendary(Module):
    """Legendary Speed 1 module."""

    energy_consumption = MODULE_DICT["Speed module"]["energy_consumption"][4]
    pollution = MODULE_DICT["Speed module"]["pollution"][4]
    productivity = MODULE_DICT["Speed module"]["productivity"][4]
    quality = MODULE_DICT["Speed module"]["quality"][4]
    speed = MODULE_DICT["Speed module"]["speed"][4]


class Speed2Legendary(Module):
    """Legendary Speed 2 module."""

    energy_consumption = MODULE_DICT["Speed module 2"]["energy_consumption"][4]
    pollution = MODULE_DICT["Speed module 2"]["pollution"][4]
    productivity = MODULE_DICT["Speed module 2"]["productivity"][4]
    quality = MODULE_DICT["Speed module 2"]["quality"][4]
    speed = MODULE_DICT["Speed module 2"]["speed"][4]


class Speed3Legendary(Module):
    """Legendary Speed 3 module."""

    energy_consumption = MODULE_DICT["Speed module 3"]["energy_consumption"][4]
    pollution = MODULE_DICT["Speed module 3"]["pollution"][4]
    productivity = MODULE_DICT["Speed module 3"]["productivity"][4]
    quality = MODULE_DICT["Speed module 3"]["quality"][4]
    speed = MODULE_DICT["Speed module 3"]["speed"][4]
