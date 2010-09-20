export PERL5LIB=../../../pegex-pm/lib
ALL_PEGEX = $(shell ls *.pgx | grep -v cdent)
ALL_YAML = $(ALL_PEGEX:%.pgx=%.pgx.yaml)
COMPILE_COMMAND = perl -MPegex::Compiler::Bootstrap -e 'print Pegex::Compiler::Bootstrap->new->compile_file(shift)->combinate->to_yaml'

all: $(ALL_YAML)

%.pgx.yaml: %.pgx
	$(COMPILE_COMMAND) $< > $@
