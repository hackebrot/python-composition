# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Defines the role interface and concrete implementations."""

from __future__ import annotations

from typing_extensions import Protocol

from composition.person import Profile
from composition.project import Project


class Role(Protocol):
    """Interface for roles a team member can take."""

    expertise: str

    def work_on_project(self, profile: Profile, project: Project) -> None:
        """Roles define the work for the respective role."""


class OperationsEngineer:
    """Role for team members with expertise in operations."""

    expertise = "📦"

    def work_on_project(self, profile: Profile, project: Project) -> None:
        """Work on the given project."""
        print(f"{profile} maintains systems software for {project}. {self.expertise}")


class DataScientist:
    """Role for team members with expertise in data science."""

    expertise = "📈"

    def work_on_project(self, profile: Profile, project: Project) -> None:
        """Work on the given project."""
        print(f"{profile} analyzes data to improve {project}. {self.expertise}")


class ProjectManager:
    """Role for team members with expertise in project management."""

    expertise = "📝"

    def work_on_project(self, profile: Profile, project: Project) -> None:
        """Work on the given project."""
        print(
            f"{profile} plans and oversees activities for {project}. {self.expertise}"
        )


class MobileEngineer:
    """Role for team members with expertise in mobile platforms."""

    expertise = "📱"

    def work_on_project(self, profile: Profile, project: Project) -> None:
        """Work on the given project."""
        print(f"{profile} develops mobile applications for {project}. {self.expertise}")
