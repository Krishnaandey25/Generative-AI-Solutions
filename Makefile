.PHONY: install test lint format clean

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/

lint:
	flake8 src/
	mypy src/

format:
	black src/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf *.egg-info