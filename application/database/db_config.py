from os import getenv
from typing import Any

from dotenv import load_dotenv
load_dotenv()


def to_bool(val: Any) -> bool:
    """
    Converts a value to a boolean.
    :param val: The value to convert.
    :return: True if in 1, yes, true. False otherwise.
    """
    return str(val).lower() in ["1", "yes", "true"]


DATABASE_ENGINE = getenv("DB_ENGINE")
DATABASE_ECHO = to_bool(getenv("DB_ECHO", False))