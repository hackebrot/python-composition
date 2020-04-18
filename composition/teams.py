# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Defines a project member class and a collection of factory functions."""

from __future__ import annotations

from composition.person import Profile
from composition.project import Project
from composition.roles import Role
from composition.stay_hydrated import StayHydrated
from composition.workplaces import Workplace


class TeamMember:
    """Composite class for members of a team."""

    def __init__(
        self,
        profile: Profile,
        role: Role,
        workplace: Workplace,
        stay_hydrated: StayHydrated,
    ):
        self.profile = profile
        self.role = role
        self.workplace = workplace
        self.stay_hydrated = stay_hydrated

    def work_on_project(self, project: Project) -> None:
        """Start working on the given project."""

        with self.workplace.commute(self.profile):
            self.role.work_on_project(self.profile, project)
            self.stay_hydrated.drink(self.profile)

    def go_to_the_movies(self) -> None:
        print(f"{self.profile} goes to the movies. 🍿")

    def go_hiking(self) -> None:
        print(f"{self.profile} goes hiking. ⛰")

    def build_a_robot(self) -> None:
        print(f"{self.profile} builds a robot. 🤖")
