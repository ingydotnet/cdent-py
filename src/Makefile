ALL = base perl python
ALL_GRAMMAR_MODULES = $(ALL:%=../cdent/parser/%/grammar.py)
ALL_DIRS = $(ALL:%=../cdent/parser/%/)
ALL_INDEX = $(ALL:%=../cdent/parser/%/__init__.py)

all: $(ALL_DIRS) $(ALL_INDEX) $(ALL_GRAMMAR_MODULES)

../cdent/parser/%/grammar.py: grammar/%.yaml ../cdent/parser/%/
	bin/grammar-module $< > $@

$(ALL_DIRS):
	mkdir -p $@

$(ALL_INDEX):
	touch $@

clean:
	rm -fr $(ALL_DIRS)
