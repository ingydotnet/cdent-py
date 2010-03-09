import os

cmds = [
    'PYTHONPATH=lib python cdent --compile --from=cd --to=py --input=hello-world/World.cd',
    'PYTHONPATH=lib python cdent --compile --from=cd --to=pm --input=hello-world/World.cd',
    'PYTHONPATH=lib python cdent --compile --from=cd --to=js --input=hello-world/World.cd',
    'cd hello-world; python hello_world.py',
    'cd hello-world; perl hello_world.pl',
    'cd hello-world; js hello_world.js',
]

for cmd in cmds:
    if os.system(cmd):
        print "Command failed: '%s'" % cmd
        break
