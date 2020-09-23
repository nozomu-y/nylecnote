all: manual.pdf clean

manual.pdf: manual.tex
	xelatex manual
	xelatex manual
	xelatex manual

clean:
	rm -rf manual.aux manual.log manual.dvi manual.out manual.toc 
