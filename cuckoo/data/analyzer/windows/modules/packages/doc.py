# Copyright (C) 2012-2013 Claudio Guarnieri.
# Copyright (C) 2014-2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from _winreg import HKEY_CURRENT_USER

from lib.common.abstracts import Package

class DOC(Package):
    """LibreOffice analysis package."""
    PATHS = [
        ("ProgramFiles", "LibreOffice", "program", "soffice.exe"),
    ]

    def start(self, path):
        libreOffice = self.get_path("LibreOffice")
        return self.execute(
            libreOffice, args=[path], trigger="file:%s" % path
        )
