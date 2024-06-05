all:

test:
	poetry run pytest --ruff --ruff-format

reformat:
	poetry run ruff check --select I --fix
	poetry run ruff format
