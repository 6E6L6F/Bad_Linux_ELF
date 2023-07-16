from . import linux
from . import RepeateTime
class Main(linux.BadLinux  , RepeateTime.RepeatedTimer):
    def __init__(self) -> None:
        super().__init__()
