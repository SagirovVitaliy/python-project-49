build:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

lint:
	poetry run flake8 brain_games