# Backend

Python service for the InferGPT backend.

## Structure
- `/supervisors` storing all supervisor modules (agents that call other agents for a greater goal)
- `/agents` containing all agents the director can call. Agents have their own functions stored within the agent module
- `/utils` with all shared utility modules
- `/tools` for all shared function modules

## Set up

1. Create the `.env` files. There are template files (.env.example) for you to copy with comments for guidance. You will need a chosen LLM to run the service. If you are running the service in Docker you can skip the rest of the setup.

Unless otherwise stated all of the commands mentioned in this README should be run from `./backend`.

2. Change directory to the `/backend` space, then run the following to install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the app
```bash
uvicorn src.api:app --port 8250
```

4. Check the backend app is running at [http://localhost:8250/health](http://localhost:8250/health)

## Linting

Ruff is being used for the backend linting. See the docs: [here](https://docs.astral.sh/ruff/)

Make sure the ruff dependency is downloaded; It is defined in the `requirements.txt` so step `1` of [setup](#set-up) should do this for you.

Run the following command to check:

```bash
ruff --version
```

If it is not installed use the following command:

```bash
pip install ruff
```

If ruff is installed correctly, the python files in the backend will be checked using the following command, from the backend directory:

```bash
ruff check
```

You can run the following command to fix any errors automatically:

```bash
ruff format
```

The ruff vscode plugin can also be installed from the store to show linting errors in the IDE.

### Linting Rules

Currently there are 4 rule groups selected in`ruff.toml`. All rule groups can be found [here](https://docs.astral.sh/ruff/rules/).

To add further rules, these are added to `ruff.toml` by using the letter asssigned to the rules as in the docs linked above. ie. pep8-naming uses the letter "N".

## Test

`pytest` is being used for testing the backend. Like with linting, running the [setup](#set-up) steps should download `pytest` for you. 

We are using a separate `tests` directory to store all the tests. This directory is intended to mirror the `src` directory to make it easier to find the tests for a specific module.

> [!WARNING]  
> running the `pytest` tests only works when running the service locally (not through the Docker setup)

To run the tests, change to the `/backend` directory and run the following command:

```bash
pytest
```

More documentation on `pytest` can be found [here](https://docs.pytest.org/en/8.0.x/).

## Contributing

### Type errors

The vscode extension [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) can be used to highlight basic type errors in your python code. To set this up do the following:

- Install the extension
- Add the following to your `../.vscode/settings.json` file:

```json
{
    "python.analysis.typeCheckingMode": "basic",
}
```