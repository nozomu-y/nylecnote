all: manual clean

manual: 
	uplatex manual.tex
	uplatex manual.tex
	dvipdfmx manual

clean:
	rm -rf manual.aux manual.log manual.dvi manual.out manual.toc 
