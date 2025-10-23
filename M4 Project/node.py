#Node Data Class
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


