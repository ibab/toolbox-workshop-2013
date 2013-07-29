
slides.pdf: slides.tex beamerthemeTU.sty contents/intro.tex contents/unix.tex contents/git.tex contents/python.tex contents/libraries.tex
	lualatex --shell-escape slides.tex
	lualatex --shell-escape slides.tex

show: slides.pdf
	mimeopen slides.pdf

clean:
	rm -rf *.log
	rm -rf *.out
	rm -rf *.toc
	rm -rf *.snm
	rm -rf *.aux
	rm -rf *.nav
	rm -rf *.vrb
	rm -rf slides.pdf
