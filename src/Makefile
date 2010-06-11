ALL = python perl6 javascript pir
ALL_GRAMMAR_MODULES = $(ALL:%=../cdent/parser/%/grammar.py)
ALL_DIRS = $(ALL:%=../cdent/parser/%/)
ALL_INDEX = $(ALL:%=../cdent/parser/%/__init__.py)

all: $(ALL_DIRS) $(ALL_INDEX) $(ALL_GRAMMAR_MODULES)

../cdent/parser/%/grammar.py: grammar/%.yaml ../cdent/parser/%/ always
	bin/grammar-module grammar/base.yaml $< > $@

$(ALL_DIRS):
	mkdir -p $@

$(ALL_INDEX):
	touch $@

clean:
	rm -fr $(ALL_GRAMMAR_MODULES)

always:
