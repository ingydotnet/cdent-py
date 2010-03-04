.PHONY: java cpp

CLASSPATH = .

default:
	@echo 'make java                  # Compile the Java example'
	@echo 'make cpp                   # Compile the C++ example'

java: hello_world.class

# javarun: hello_world.class
# 	CLASSPATH=$(CLASSPATH) java hello_world

hello_world.class: hello_world.java World.class
	CLASSPATH=$(CLASSPATH) javac $<

World.class: World.java
	CLASSPATH=$(CLASSPATH) javac $<

# C++ stuff in progress.
cpp: hello_world

hello_world: hello_world.o
	mv $< $@

clean:
	rm -fr *.class *.pyc *.o hello_world

