# latest Working power terminal

'poetry --version'
'poetry new project_002'
'cd project_002'
'poetry run python --version'
'poetry add requests'
'poetry run python project_002/main.py'
'poetry add pytest'
'poetry run pytest'
'poetry run pytest -v'

 PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform> cd 01_micro_create_project
 PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project> ls
Mode                 LastWriteTime         Length Name
d-----         3/22/2024  10:13 PM                project_001
d-----         3/22/2024   8:56 PM                test_poetry

PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project> poetry --version Poetry could not find a pyproject.toml file in C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project or its parents                                                                      etry run python --version
PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project> poetry new project_002                                                                         in_one_platform\01_micro_crea
Created package project_002 in project_002
PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project> cdetry new project_002 project_002
PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project\pro project_002ject_002> poetry run python --version   ject_002> poetry run python --
Creating virtualenv project-002-Ai4TPfXb-py3.12 in C:\Users\Batch37PIAIC\AppData\Local\pypoetry\Cache\virtualenvs
Python 3.12.2
PS C:\Users\Batch 37  PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project\project_002> poetry env list project-002-Ai4TPfXb-py3.12 (Activated)
PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project\project_002> poetry add requests
Using version ^2.32.3 for requests

Updating dependencies
Resolving dependencies... (3.2s)

Package operations: 5 installs, 0 updates, 0 removals

- Installing certifi (2024.7.4)
- Installing charset-normalizer (3.3.2)
- Installing idna (3.7)
- Installing urllib3 (2.2.2)
- Installing requests (2.32.3)

Writing lock file
PS C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project\project_002> poetry run python project_002/main.py
Hello World

01_micro_create_project\projecoject\project_002> poetry add pytest
Using version ^8.3.1 for pytest
Updating dependencies
Resolving dependencies... (1.0s)
Package operations: 4 installs, 0 updates, 0 removals

- Installing iniconfig (2.0.0)
- Installing packaging (24.1)
- Installing pluggy (1.5.0)
- Installing pytest (8.3.1)

Writing lock file

01_micro_create_project\project_002> poetry run pytest
=============================================== test session starts ===============================================
platform win32 -- Python 3.12.2, pytest-8.3.1, pluggy-1.5.0
rootdir: C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project\project_002
configfile: pyproject.toml
collected 2 items

tests\test_myproject.py ..                       [100%]
================================= 2 passed in 0.11s ==================================
01_micro_create_project\project_002> poetry run pytest -v
=============================================== test session starts ===============================================
platform win32 -- Python 3.12.2, pytest-8.3.1, pluggy-1.5.0 -- C:\Users\Batch 37 PIAIC\AppData\Local\pypoetry\Cache\virtualenvs\project-002-Ai4TPfXb-py3.12\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Batch 37 PIAIC\generative-ai\learn-generative-ai\05_microservices_all_in_one_platform\01_micro_create_project\project_002
configfile: pyproject.toml
collected 2 items

tests/test_myproject.py::test_function1 PASSED                                                               [ 50%]
tests/test_myproject.py::test_function2 PASSED                                                               [100%]
======================================= 2 passed in 0.08s =======================================
