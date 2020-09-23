all: manual clean

manual: 
	xelatex manual
	xelatex manual
	xelatex manual

clean:
	rm -rf manual.aux manual.log manual.dvi manual.out manual.toc 
