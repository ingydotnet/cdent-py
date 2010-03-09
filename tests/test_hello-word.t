import os

cmds = [
    'PYTHONPATH=lib python cdent --compile --from=cd --to=py --input=hello-world/World.cd',
    'PYTHONPATH=lib python cdent --compile --from=cd --to=pm --input=hello-world/World.cd',
    'PYTHONPATH=lib python cdent --compile --from=cd --to=js --input=hello-world/World.cd',
    'cd hello-world; python hello_world.py',
    'cd hello-world; perl hello_world.pl',
    'cd hello-world; ruby hello_world.rb',
    'cd hello-world; js hello_world.js',
    'cd hello-world; php hello_world.php',
    'cd hello-world; python3 hello_world.py3',
    'cd hello-world; perl6 hello_world.p6',
    '# Done',
]

for cmd in cmds:
    print cmd
    if os.system(cmd):
        print "Command failed: '%s'" % cmd
        break
