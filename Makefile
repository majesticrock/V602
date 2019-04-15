all: build/main.pdf
build/ekz.pdf: ekz.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python ekz.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/ekz.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
