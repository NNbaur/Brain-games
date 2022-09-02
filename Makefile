install:
	poetry install

brain-games:
	poetry run brain-game

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

uninstall:
	python3 -m pip uninstall brain_games-0.1.0-py3-none-any.whl
