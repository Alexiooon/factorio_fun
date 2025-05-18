"""Module for handling science progress.

The module provides a global tracker of research in the form of a singleton
class. This is to allow separate modules (mostly crafting stations) to access
the bonus productivity without being handled by the user (Except for setting the
global level of course).

It is initialized at module import, and defaults to 0 in all productivity
researches. This way it will not interfere with any calculations unless other
values are set during runtime. There are NO other parts of the module which
automatically sets research level(s), so one can be sure that it is only set to
what is explicitly specified. Otherwise things would be a mess...

Future work might add the possibility to create local copies to e.g. compare different levels.
"""

from .constants import QualityLevel

# Valid types of productivity research
PRODUCTIVITY_OPTIONS = (
    "Asteroid",
    "Low density structure",
    "Mining",
    "Plastic bar",
    "Processing unit",
    "Research",
    "Rocket fuel",
    "Rocket part",
    "Scrap recycling",
    "Steel plate",
)


class ScienceSingleton:
    """Science progress tracker, using the singleton pattern as to only allow a single instance."""

    class ScienceSingletonInstance:
        """Science progress tracker instance."""

        def __init__(self) -> None:
            """Init."""
            self.max_quality = QualityLevel.RARE
            self._productivity_dict = {research_type: 0 for research_type in PRODUCTIVITY_OPTIONS}

        @staticmethod
        def _validate_arguments(science: str = "", level: int = 0) -> None:
            """Validate whether input arguments are valid and raises a ValueError if not."""
            if science not in PRODUCTIVITY_OPTIONS and not science:
                raise ValueError(f'"Science" argument must be one of: {PRODUCTIVITY_OPTIONS}')
            if not int(level) >= 0:
                raise ValueError("Productivity level must be a positive integer.")

        def load(self, science_dict: dict[str:int]) -> None:
            """Set multiple science levels at once.

            Args:
              science_dict: Dictionary with keys as research type and values as levels.

            Raises:
              ValueError: If any of the keys or values of science_dict are invalid.
            """
            for science, level in science_dict.items():
                self._validate_arguments(science, level)
                self._productivity_dict[science] = level

        def set_research_level(self, science: str, level: int) -> None:
            """Set the latest researched level of a type of productivity.

            Args:
              science: String with the productivity research to set. Valid options are:
                "Asteroid"
                "Low density structure"
                "Mining"
                "Plastic bar"
                "Processing unit"
                "Research"
                "Rocket fuel"
                "Rocket part"
                "Scrap recycling"
                "Steel plate"
              level: Integer for the finished research level.

            Raises:
             - ValueError: If either of the arguments are invalid
            """
            self._validate_arguments(science, level)
            self._productivity_dict[science] = int(level)

        def get_research_level(self, science: str) -> int:
            """Set the latest researched level of a type of productivity.

            Args:
              science: String with the productivity research to set. Valid options are:
                "Asteroid"
                "Low density structure"
                "Mining"
                "Plastic bar"
                "Processing unit"
                "Research"
                "Rocket fuel"
                "Rocket part"
                "Scrap recycling"
                "Steel plate"
              level: Integer for the finished research level.

            Raises:
             - ValueError: If either of the arguments are invalid
            """
            self._validate_arguments(science)
            return self._productivity_dict.get(science, 0)  # Return 0 if it doesn't exist

    # Storage of the instance reference
    __instance = None

    def __init__(self):
        """Initialize singleton instance."""
        if ScienceSingleton.__instance is None:
            ScienceSingleton.__instance = ScienceSingleton.ScienceSingletonInstance()

        # Store instance reference as the only member in the handle
        self.__dict__["_EQSingleton__instance"] = ScienceSingleton.__instance

    def __getattr__(self, attr):
        """Delegate access to implementation."""
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """Delegate access to implementation."""
        return setattr(self.__instance, attr, value)


GlobalScienceProgress = ScienceSingleton()
