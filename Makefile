## Format your code using black
.PHONY: black
black:
	python -m black --version
	python -m black .