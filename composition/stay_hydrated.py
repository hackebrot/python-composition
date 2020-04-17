# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Define the StayHydrated interface and concrete implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod


class StayHydrated(ABC):
    """Interface for ways to stay hydrated."""

    @abstractmethod
    def drink(self, person: str) -> None:
        """Subclasses define what a person drinks."""


class DrinkWater(StayHydrated):
    def drink(self, person: str) -> None:
        """Drink some water."""
        print(f"{person} drinks some water. 🚰")


class DrinkTea(StayHydrated):
    def drink(self, person: str) -> None:
        """Drink some tea."""
        print(f"{person} drinks tea. 🍵")
