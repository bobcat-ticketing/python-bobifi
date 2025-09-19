all:

test:
	uv run pytest --ruff --ruff-format

reformat:
	uv run ruff check --select I --fix
	uv run ruff format
