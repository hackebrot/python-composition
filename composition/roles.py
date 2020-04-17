# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Defines the role interface and concrete implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod

from projects import Project


class Role(ABC):
    """Interface for roles a team member can take."""

    @property
    @abstractmethod
    def expertise(self):
        """Subclasses return the expertise of the respective role."""

    @abstractmethod
    def work_on_project(self, person: str, project: Project) -> None:
        """Subclasses define the work for the respective role."""


class OperationsEngineer(Role):
    """Role for team members with expertise in operations."""

    def work_on_project(self, person: str, project: Project) -> None:
        """Work on the given project."""
        print(f"{person} maintains systems software for {project}. {self.expertise}")

    @property
    def expertise(self) -> str:
        """Return the expertise for the operations engineer role."""
        return "📦"


class DataScientist(Role):
    """Role for team members with expertise in data science."""

    def work_on_project(self, person: str, project: Project) -> None:
        """Work on the given project."""
        print(f"{person} analyzes data to improve {project}. {self.expertise}")

    @property
    def expertise(self) -> str:
        """Return the expertise for the data scientist role."""
        return "📈"


class ProjectManager(Role):
    """Role for team members with expertise in project management."""

    def work_on_project(self, person: str, project: Project) -> None:
        """Work on the given project."""
        print(f"{person} plans and oversees activities for {project}. {self.expertise}")

    @property
    def expertise(self) -> str:
        """Return the expertise for the project manager role."""
        return "📝"
