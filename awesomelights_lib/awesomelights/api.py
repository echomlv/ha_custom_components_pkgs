# awesomelights/api.py

"""awesomelights.py (模拟外部库)."""

import logging
import random

_LOGGER = logging.getLogger(__name__)


class AwesomeLight:
    """Represents a single light device in the AwesomeLights system."""

    def __init__(self, name: str, initial_brightness: int = 128) -> None:
        """Initialize the light."""
        self.name = name
        self._is_on = random.choice([True, False])  # Random initial state
        self._brightness = initial_brightness if self._is_on else 0
        _LOGGER.info(
            "AwesomeLight '%s' initialized. State: %s, Brightness: %d",
            self.name,
            self._is_on,
            self._brightness,
        )

    def turn_on(self) -> None:
        """Simulate turning the light on."""
        self._is_on = True
        # If brightness was 0, set it to a default value (e.g., 255)
        if self._brightness == 0:
            self._brightness = 255
            _LOGGER.info(
                "AwesomeLight '%s' turned ON. Brightness: %d",
                self.name,
                self._brightness,
            )

    def turn_off(self) -> None:
        """Simulate turning the light off."""
        self._is_on = False
        self._brightness = 0
        _LOGGER.info("AwesomeLight '%s' turned OFF", self.name)

    def update(self) -> None:
        """Simulate fetching the latest state from the device."""
        # In a real library, this would be an API call.
        # Here we just log the current state.
        _LOGGER.debug(
            "AwesomeLight '%s' state updated: %s, Brightness: %d",
            self.name,
            self.is_on(),
            self.brightness,
        )

    def is_on(self) -> bool:
        """Return the current on/off state."""
        return self._is_on

    @property
    def brightness(self) -> int:
        """Get the current brightness (0-255)."""
        return self._brightness

    @brightness.setter
    def brightness(self, value: int) -> None:
        """Set the brightness (0-255)."""
        self._brightness = max(0, min(255, value))
        # Ensure light is considered 'on' if brightness > 0
        if self._brightness > 0:
            self._is_on = True
        else:
            self._is_on = False
        _LOGGER.info(
            "AwesomeLight '%s' brightness set to %d", self.name, self._brightness
        )


class Hub:
    """Represents the AwesomeLights Hub, responsible for connecting and listing devices."""

    def __init__(self, host: str, username: str, password: str | None = None) -> None:
        """Initialize the Hub with connection details."""
        self._host = host
        self._username = username
        self._password = password
        _LOGGER.info("Connecting to Hub at %s as %s", self._host, self._username)

    def is_valid_login(self) -> bool:
        """Simulate login validation."""
        # For demo, we always return True unless the host is 'badhost'
        if self._host == "badhost":
            _LOGGER.error("Simulated login failure for badhost")
            return False
        _LOGGER.info("Simulated login successful")
        return True

    def lights(self) -> list[AwesomeLight]:
        """Return a list of discovered lights."""
        # Simulate discovering a few lights
        return [
            AwesomeLight("Living Room Light"),
            AwesomeLight("Kitchen Counter Light", initial_brightness=200),
            AwesomeLight("Bedroom Lamp"),
        ]
