# actor-critic-pet

## Use local

- `make env [python=3.12]` create dev python environment.
- `make serve` build and up docker stack.
- `make up` up docker stack.
- `make down` down docker stack.
- `make check` tests, lint and mypy all.
- `make config` show docker stack info.
- `make create path=src/module.py [pr=prompt1[,prompt2,...]]` - create a python file with optional prompt header.
- `make clean path=src/module.py` - Remove leading triple-quoted comment block from python file.
- `poetry install --with dev --no-root` install poetry dependencies

Use `research` folder for experiments.

Use `prompts` folder for llm system prompts.
