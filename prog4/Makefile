default: prog4

prog4: prog4.c check.o
	gcc -std=c99 -g prog4.c check.o -o prog4 -lm


check.o: check.c
	gcc -std=c99 -c check.c -o check.o -lm

clean:
	-rm -f prog4

