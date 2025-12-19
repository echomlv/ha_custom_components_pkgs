# awesomelights/api.py

"""awesomelights.py (模拟外部库)."""

import ctypes
import logging
from pathlib import Path
import random

_LOGGER = logging.getLogger(__name__)

# ----------------------------------------------------
# 1. 加载 C 驱动
# 假设 awesome_c_driver.so 位于与此文件相同的目录或可访问的路径
try:
    # 1. 获取当前文件的目录路径
    # Path(__file__).parent 相当于 os.path.dirname(__file__)
    current_dir = Path(__file__).parent

    # 2. 使用 / 运算符拼接路径 (更自然、更安全)
    C_DRIVER_PATH = current_dir / "awesome_c_driver.so"

    # 3. 检查路径是否存在，并转换为字符串供 ctypes 使用
    if not C_DRIVER_PATH.exists():
        # 如果找不到，尝试加载全局路径
        C_DRIVER_PATH = Path("awesome_c_driver.so")

    # ctypes.CDLL 需要一个字符串或 PathLike 对象
    # Path 对象通常被 ctypes 正确接受
    _C_DRIVER = ctypes.CDLL(str(C_DRIVER_PATH))
    _LOGGER.info("C Driver loaded successfully from %s", C_DRIVER_PATH)

except OSError as e:  # 修正: 捕获更具体的 OSError
    # 针对 ctypes.CDLL 失败的常见错误
    _LOGGER.error(
        "Failed to load C driver: %s. Check file path/permissions/bitness. Integration will fail",
        e,
    )
    _C_DRIVER = None
except Exception as e:
    # 保留一个更宽泛的捕获，以防 ctypes.CDLL 抛出非 OSError 的错误，但这是次要的。
    # 规范的做法是仅捕获您预期的异常类型。
    _LOGGER.error("An unexpected error occurred during C driver loading: %s", e)
    _C_DRIVER = None


# 2. 定义 C 函数的签名和返回类型
if _C_DRIVER:
    # get_state() -> int (bool)
    _C_DRIVER.get_state.restype = ctypes.c_int

    # get_brightness() -> int
    _C_DRIVER.get_brightness.restype = ctypes.c_int

    # turn_on() -> void
    _C_DRIVER.turn_on.restype = None

    # turn_off() -> void
    _C_DRIVER.turn_off.restype = None

    # set_brightness(int value) -> void
    _C_DRIVER.set_brightness.argtypes = [ctypes.c_int]
    _C_DRIVER.set_brightness.restype = None


# ----------------------------------------------------
# 3. Python 封装类 (AwesomeLight 和 Hub)


class AwesomeLight:
    """Python wrapper for the C-driven light."""

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

        if _C_DRIVER:
            _C_DRIVER.turn_on()

    def turn_off(self) -> None:
        """Simulate turning the light off."""

        if _C_DRIVER:
            _C_DRIVER.turn_off()

    def update(self) -> None:
        """Simulate fetching the latest state from the device."""

        # C 驱动是全局状态，无需更新，但保留结构

    def is_on(self) -> bool:
        """Return the current on/off state."""

        if _C_DRIVER:
            return bool(_C_DRIVER.get_state())
        return False

    @property
    def brightness(self) -> int:
        """Get the current brightness (0-255)."""
        if _C_DRIVER:
            return _C_DRIVER.get_brightness()
        return 0

    @brightness.setter
    def brightness(self, value: int) -> None:
        if _C_DRIVER:
            _C_DRIVER.set_brightness(value)


class Hub:
    """Manages connection and devices."""

    def __init__(self, host: str, username: str, password: str | None = None) -> None:
        """Initialize the Hub with connection details."""

        # 无需连接，驱动已加载

    def is_valid_login(self) -> bool:
        """Simulate login validation."""

        return _C_DRIVER is not None

    def lights(self) -> list[AwesomeLight]:
        """返回 C 驱动控制的单个灯光."""
        if self.is_valid_login():
            return [
                AwesomeLight("Living Room Light"),
                AwesomeLight("Kitchen Counter Light", initial_brightness=200),
                AwesomeLight("Bedroom Lamp"),
            ]
        return []
