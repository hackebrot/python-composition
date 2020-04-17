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
    """Workplace for team members working from the office."""

    @contextmanager
    def commute(self, person: str) -> Generator:
        """Commute to the office and back home."""
        print(f"{person} commutes to the office. 🏢")
        yield
        print(f"{person} commutes home. 🏡")


class Home(Workplace):
    """Workplace for team members working from home."""

    @contextmanager
    def commute(self, person: str) -> Generator:
        """Get ready for work at home."""
        print(f"{person} works from home. 🏡")
        yield


class Remote(Workplace):
    """Workplace for team members working remotely."""

    def __init__(self, workplace: str):
        self.workplace = workplace

    @contextmanager
    def commute(self, person: str) -> Generator:
        """Commute to the workplace and back home."""
        print(f"{person} commutes to {self.workplace}. 🚌")
        yield
        print(f"{person} commutes home. 🏡")
