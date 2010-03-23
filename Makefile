.PHONY: default build test install register sdist clean upload

default:
	@echo 'No default action for make'

build test install register sdist clean::
	python setup.py $@

upload:: clean register
	python setup.py sdist $@

clean::
	find . -name '*.pyc' | xargs rm
	rm -fr build dist MANIFEST
