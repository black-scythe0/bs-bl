FLAGS = -Wall -Wextra -Wimplicit
COMPILER = cc

SOURCE = bsbl.c hello.c
OBJECT = bsbl.o hello.o
OUTPUT = bs-blc

%.o: src/%.c
	$(COMPILER) -o $@ -c $(FLAGS) $<


make: 
	$(COMPILER) -o $(OUTPUT) $(OBJECT)  
    
.PHONY: clean
clean:
	rm -rf *.o
