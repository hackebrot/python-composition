# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Example project for composition over inheritance in Python."""

from __future__ import annotations

from composition.person import Profile
from composition.project import Project
from composition.roles import (
    DataScientist,
    MobileEngineer,
    OperationsEngineer,
    ProjectManager,
)
from composition.stay_hydrated import DrinkTea, DrinkWater
from composition.teams import TeamMember
from composition.workplaces import Home, Office, Remote

if __name__ == "__main__":
    simone = TeamMember(
        profile=Profile(name="Simone", emoji="👸🏼"),
        role=OperationsEngineer(),
        workplace=Office(),
        stay_hydrated=DrinkWater(),
    )

    # simone.go_to_the_movies()
    # simone.build_a_robot()
    # simone.go_hiking()

    data_platform = Project(
        board_name="Data Platform",
        description="Platform providing datasets and data viewing tools.",
    )

    dave = TeamMember(
        profile=Profile(name="Dave", emoji="🧙🏽‍♂️"),
        role=ProjectManager(),
        workplace=Remote(workplace="a local coffee shop"),
        stay_hydrated=DrinkWater(),
    )

    chelsea = TeamMember(
        profile=Profile(name="Chelsea", emoji="🐶"),
        role=DataScientist(),
        workplace=Office(),
        stay_hydrated=DrinkTea(),
    )

    marlene = TeamMember(
        profile=Profile(name="Marlene", emoji="👩🏿‍💻"),
        role=MobileEngineer(),
        workplace=Home(),
        stay_hydrated=DrinkTea(),
    )

    team = [simone, dave, chelsea, marlene]

    # Everyone is strongly recommended to work from home. What now? 😨
    for team_member in team:
        team_member.workplace = Home()
        team_member.work_on_project(data_platform)
