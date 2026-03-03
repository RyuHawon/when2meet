import string
from typing import Final


class Base62:
    BASE: Final[str] = string.ascii_letters + string.digits
    BASE_LEN: Final[int] = len(BASE)
    print(BASE_LEN)
