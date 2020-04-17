# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Example project for composition over inheritance in Python."""

from __future__ import annotations

from profiles import Profile
from projects import Project
from roles import DataScientist, OperationsEngineer, ProjectManager
from stay_hydrated import DrinkTea, DrinkWater
from teams import TeamMember
from workplaces import Home, Office, Remote


def new_operations_engineer(name: str, emoji: str) -> TeamMember:
    """Create a new team member with expertise in operations."""
    return TeamMember(
        profile=Profile(name=name, emoji=emoji),
        role=OperationsEngineer(),
        workplace=Office(),
        stay_hydrated=DrinkWater(),
    )


def new_data_scientist_who_likes_tea(name: str, emoji: str) -> TeamMember:
    """Create a new team member with expertise in data science and drinks tea."""
    return TeamMember(
        profile=Profile(name=name, emoji=emoji),
        role=DataScientist(),
        workplace=Office(),
        stay_hydrated=DrinkTea(),
    )


def new_project_manager_who_works_remotely(
    name: str, emoji: str, workplace: str
) -> TeamMember:
    """Create a new team member with expertise in project management."""

    if workplace == "home":
        workplace_instance = Home()
    else:
        workplace_instance = Remote(workplace)

    return TeamMember(
        profile=Profile(name=name, emoji=emoji),
        role=ProjectManager(),
        workplace=workplace_instance,
        stay_hydrated=DrinkWater(),
    )


if __name__ == "__main__":
    simone = new_operations_engineer(name="Simone", emoji="👸🏼")

    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()

    data_platform = Project(
        board_name="Data Platform",
        description="Platform providing datasets and data viewing tools.",
    )

    chelsea = new_data_scientist_who_likes_tea(name="Chelsea", emoji="🐶")

    dave = new_project_manager_who_works_remotely(
        name="Dave", emoji="🧙🏽‍♂️", workplace="a local coffee shop"
    )

    simone.work_on_project(data_platform)
    chelsea.work_on_project(data_platform)
    dave.work_on_project(data_platform)
