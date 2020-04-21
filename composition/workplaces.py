# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Defines the workplace interface and concrete implementations."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator, Iterator

from typing_extensions import ContextManager, Protocol

from composition.person import Profile


class Workplace(Protocol):
    """Interface for workplaces."""

    @contextmanager
    def commute(self, profile: Profile) -> Iterator[None]:
        """Implementations define how a person commutes to the workplace."""


class Office:
    """Workplace for team members working from the office."""

    @contextmanager
    def commute(self, profile: Profile) -> Iterator[None]:
        """Commute to the office and back home."""
        print(f"{profile} commutes to the office. 🏢")
        yield
        print(f"{profile} commutes home. 🏡")


class Home:
    """Workplace for team members working from home."""

    @contextmanager
    def commute(self, profile: Profile) -> Iterator[None]:
        """Get ready for work at home."""
        print(f"{profile} works from home. 🏡")
        yield


class Remote:
    """Workplace for team members working remotely."""

    def __init__(self, workplace: str):
        self.workplace = workplace

    @contextmanager
    def commute(self, profile: Profile) -> Iterator[None]:
        """Commute to the workplace and back home."""
        print(f"{profile} commutes to {self.workplace}. 🚌")
        yield
        print(f"{profile} commutes home. 🏡")
