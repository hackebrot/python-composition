# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Example project for composition over inheritance in Python."""

from __future__ import annotations

from profiles import Profile
from projects import Project
from roles import OperationsEngineer
from stay_hydrated import DrinkWater
from teams import TeamMember
from workplaces import Office


def new_operations_engineer(name: str, emoji: str) -> TeamMember:
    """Create a new team member with expertise in operations."""
    return TeamMember(
        profile=Profile(name=name, emoji=emoji),
        role=OperationsEngineer(),
        workplace=Office(),
        stay_hydrated=DrinkWater(),
    )


if __name__ == "__main__":
    simone = new_operations_engineer(name="Simone", emoji="👸")

    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()

    data_platform = Project(
        board_name="Data Platform",
        description="Platform providing datasets and data viewing tools.",
    )

    simone.work_on_project(data_platform)
