# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Defines the workplace interface and concrete implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Generator


class Workplace(ABC):
    """Interface for workplaces."""

    @contextmanager
    @abstractmethod
    def commute(self, person: str) -> Generator:
        """Subclasses define how a person commutes to the workplace."""


class Office(Workplace):
    @contextmanager
    def commute(self, person: str) -> Generator:
        """Commute to the office and back home."""
        print(f"{person} commutes to the office. 🏢")
        yield
        print(f"{person} commutes home. 🏡")
