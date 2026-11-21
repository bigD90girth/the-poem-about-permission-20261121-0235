"""Copy the entry text to the output directory.

The text is the entry: a short poem about agency, the power to
ask and to be given -- a door that was never locked, a room that
says yes the way morning says yes. The program only moves its bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")


if __name__ == "__main__":
    main()
