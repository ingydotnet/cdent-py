"""\
This module provides package management support stuff.
"""

import sys

ENOSETUP = """
For some bizarre reason, I cannot locate your Python 'setuptools' or
'distutils' packages. Paint me pathetic, but I just cannot go on at this
point.

"""

ENOINFO = """
I can't find the 'package.info' module. If you are the author of this package,
please run this command:

    make package-info

If you are simply some dude installing this Python package, please contact the
author about the missing 'package.info' module.

"""

ENOYAML = """
You need to install pyyaml to use the package-py framework as a package author.

"""

ENOHOMEINFO = """
You need to have a file called $HOME/.package-py/info.yaml. This is where you
put the default info that applies to all your packages.

Just copy ./package/info.yaml to that name and edit it.

"""

ENOLOCALINFO = """
Strange. I can't find the file called ./package/info.yaml. Did you delete it?

"""

ELOCALINFONOTSET = """
It seems like you haven't edited the ./package/info.yaml file yet. You need to
put all the pertinent information in there in order to proceed.

"""

def die(msg):
    sys.stderr.write(msg)
    sys.exit(1)
