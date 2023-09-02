# DB Project
This is a database visualization for the COSC-61 final project.

# Project Site
More information about the project and motivation can be found on the [Project Notion site](https://www.notion.so/Database-Visualization-7640b7c91e8e4fb5b1cfe8449280e732?pvs=4).

# Building and Running

## Frontend
The frontend uses the [PNPM](https://pnpm.io/) package manager. Use `pnpm install` or `pnpm i` in the db-frontend folder to install all packages from the `package.json`.

Libraries include:
- [D3](https://d3js.org/)
- [Svelte](https://svelte.dev/)

The frontend can be run with the command `pnpm run dev -- --open` from the db-frontend folder. 
Unless otherwise specified or already taken, the client should run on `http://localhost:5173`.

## Backend
The backend uses the [Pipenv](https://github.com/pypa/pipenv) package and version management solution (combination of pip package management and venv virtual environments).
Use `pipenv install` or `pipenv sync` in the backend folder to install all packages from the `Pipfile`.

Libraries include:
- [FastAPI](https://fastapi.tiangolo.com/)
- Uvicorn
- [PyMySQL](https://github.com/PyMySQL/PyMySQL)

The backend can be run with the command `uvicorn main:app --reload` from the backend folder.
Unless otherwise specified or already taken, the backend should run on `http://localhost:8000`.
If running with a non-standard port alongside the frontend, edit the `SERVER_PUBLIC_IP` definition in `constants.ts` to match the port and IP of the server.
