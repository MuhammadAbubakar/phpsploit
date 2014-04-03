import os
from shutil import which
from ui.color import colorize


class Executable(str):
    """Executable program or shell command. (extends str)

    Takes an executable program path or shell command.

    >>> text_editor = Executable('vim')
    >>> text_editor()
    "/usr/bin/vim"

    """
    def __new__(cls, executable):
        abspath = which( str(executable) ) # use shutil.which
        if abspath is None:
            raise ValueError("«%s» is not an executable program" %executable)
        return str.__new__(cls, abspath)


    def _raw_value(self):
        return super().__str__()


    def __call__(self):
        return self._raw_value()


    def __str__(self):
        path, name = os.path.split(self)
        path += os.sep
        name, ext = os.path.splitext(name)

        return colorize('%Cyan', path, '%BoldWhite', name, '%BasicCyan')
