from fastapi.testclient import TestClient
from fastapi_helloworld_online.main import app

def test_root_path():
    client = TestClient(app = app)
    responce = client.get("/")
    assert responce.status_code == 200
    assert responce.json() == {"Hello" : "World"}
  
def test_piaic_path():
    client = TestClient(app = app)
    responce = client.get("/piaic/")
    assert responce.status_code == 200
    assert responce.json() == {"Organization" : "PIAIC"}
   
def test_piaic_check():
    client = TestClient(app = app)
    responce = client.get("/piaic/")
    assert responce.status_code == 200
    assert responce.json() == {"Organization" : "ABC"}
