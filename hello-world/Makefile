.PHONY: java cpp

export CLASSPATH = .

default:
	@echo 'make java                  # Compile the Java example'
	@echo 'make cpp                   # Compile the C++ example'

java: hello_world.class

javarun: hello_world.class
	@java hello_world

hello_world.class: hello_world.java org/cdent/World.class
	@javac $<

org/cdent/World.class: org/cdent/World.java
	@javac $<

# C++ stuff in progress.
cpp: hello_world

hello_world: hello_world.o
	mv $< $@

clean:
	find . -name \*.class -exec rm -f {} \;
	rm -fr *.pyc *.o hello_world

