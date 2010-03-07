default:

test:
	PYTHONPATH=lib python cdent --compile --from=cd --to=js --input=hello-world/World.cd --output=output.js

# PYTHONPATH=lib python cdent --compile --from=cd --to=js --input=hello-world/World.cd --output=output.js

clean:
	rm output.js
