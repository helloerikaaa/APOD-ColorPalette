## Format your code using black
.PHONY: black
black:
	python -m black --version
	python -m black .

.PHONY: run
run:
	streamlit run src/app.py