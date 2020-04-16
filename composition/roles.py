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
