from typing import Final, ClassVar
import string


class Base62:
    BASE: Final[ClassVar[str]] = string.ascii_letters + string.digits
    BASE_LEN: Final[ClassVar[int]] = len(BASE)
    print(BASE_LEN)
