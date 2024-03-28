# modren_python Learning : PIAIC171375 Class working and practice

## Commands entered

- poetry --version
- poetry new fastapi_helloworld_online
- cd fastapi_helloworld_online
- open project in VS Code
- open project.toml file
[tool.poetry]
name = "fastapi-helloworld-online"
version = "0.1.0"
description = ""
authors = ["Hatimnofear <hatimnofear@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.110.0"
uvicorn = {extras = ["standard"], version = "^0.29.0"}

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

- install new packages in poetry project
- poetry add fastapi "uvicorn[standard]"
- create main.py and copy relative path >> fastapi_helloworld_online\fastapi_helloworld_online\main.py
- poetry shell
- Spawning shell within C:\Users\Batch 37 PIAIC\AppData\Local\pypoetry\Cache\virtualenvs\fastapi-helloworld-online-hNOBvMW--py3.12

'''
@app.get("/")
def index():
    return {"Hello" : "World"}

@app.get("/piaic/")
def piaic():
    return {"Organization" : "PIAIC"}
'''

### Running server

- poetry run uvicorn fastapi_helloworld_online.main:app --reload

- poetry add pytest
- pip install httpx

- poetry run pytest -v
