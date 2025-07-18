FLAGS = -Wall -Wextra
COMPILER = cc

SOURCE = bsLex.c
OBJECT = bsLex.o
OUTPUT = bs-blc

%.o: src/%.c
	$(COMPILER) -o $@ -c $(FLAGS) $<


make: $(OBJECT)
	$(COMPILER) -o $(OUTPUT) $<

.PHONY: clean
clean:
	rm -rf *.o
