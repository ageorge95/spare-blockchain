from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("SPARE_ROOT", "~/.spare/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("SPARE_KEYS_ROOT", "~/.spare_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(
    os.path.expanduser(os.getenv("SPARE_SIMULATOR_ROOT", f"{DEFAULT_ROOT_PATH.parent}/simulator"))
).resolve()
