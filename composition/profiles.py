# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

"""Defines a profile class."""

from __future__ import annotations


class Profile:
    """Holds personal information."""

    def __init__(self, name: str, emoji: str):
        self.name = name
        self.emoji = emoji
