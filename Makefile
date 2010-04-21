.PHONY: default build test devtest install register sdist clean upload run

ALL_TESTS = $(shell echo tests/*.py)
ALL_DEV_TESTS = $(shell echo dev-tests/*.py)

default: build

build test devtest install register sdist clean::
	python setup.py $@

upload:: clean register
	python setup.py sdist $@

tests:: $(ALL_TESTS)

$(ALL_TESTS) $(ALL_DEV_TESTS): run
	@python -c 'print " Running test: $@ ".center(70, "-") + "\n"'
	@PYTHONPATH=. python $@

clean::
	find . -name '*.pyc' | xargs rm
	rm -fr build dist MANIFEST cdent.egg-info
