# Google Cloud Function to Send Email

Exemplo de aplicação utilizando **Cloud Function**

### Virtual Enviroment
```
python3 -m venv venv

source venv/bin/activate

pip3 install --upgrade pip

pip3 install -r requirements.txt

```

### How to run?
```
functions-framework --target=hello --debug
```

### How to Deploy?
Listar os projetos existentes:
```
gcloud projects list

```
Selecionar o Project ID com o comando:
```
gcloud config set project [YOUR_PROJECT_ID]
```

Então deploy a cloud function com o comando:
```
gcloud functions deploy [FUNCTION_NAME] --runtime python37 --trigger-http
```

no caso deste problema:
```
gcloud functions deploy hello --runtime python37 --trigger-http
```

### CI/CD 
