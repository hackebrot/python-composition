# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Define the StayHydrated interface and concrete implementations."""

from __future__ import annotations

from typing_extensions import Protocol

from composition.person import Profile


class StayHydrated(Protocol):
    """Interface for ways to stay hydrated."""

    def drink(self, profile: Profile) -> None:
        """Implementations define what a person drinks."""


class DrinkWater:
    """Interface for drinking water."""

    def drink(self, profile: Profile) -> None:
        """Drink some water."""
        print(f"{profile} drinks some water. 🚰")


class DrinkTea:
    """Interface for drinking tea."""

    def drink(self, profile: Profile) -> None:
        """Drink some tea."""
        print(f"{profile} drinks tea. 🍵")
