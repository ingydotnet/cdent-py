.PHONY: default build test install register sdist clean upload run

ALL_TESTS = $(shell echo tests/*.py)

default:
	@echo 'No default action for make'

build install register sdist clean::
	python setup.py $@

upload:: clean register
	python setup.py sdist $@

test:: $(ALL_TESTS)

$(ALL_TESTS): run
	@python -c 'print " Running test: $@ ".center(70, "-") + "\n"'
	@PYTHONPATH=. python $@

clean::
	find . -name '*.pyc' | xargs rm
	rm -fr build dist MANIFEST
