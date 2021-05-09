![alt text](https://1000logos.net/wp-content/uploads/2020/10/Discord-logo.jpg) 

# Discord bot
Bot para la aplicación Discord con varias funcionalidades. Entre ellas:
* Mostrar mensajes con las normas del servidor de Discord cuando alguien nuevo entra.
* Reproducción de música en base a una URL de Youtube.
* Respuesta automática ante ciertos mensajes del chat como por ejemplo un "buenos días".
* Tirar dados
* Hacer scrape de la web https://valorant.fandom.com/wiki/ para mostrar información de un arma específica del videojuego Valorant.

### Pre-requisitos 📋

* Tendrás que crear un bot para Discord y obtener su token a través del portal de desarrollador:
https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications

## Despliegue en VM :computer:
* En el caso de no querer usar Docker para ejecutar el bot, es necesario realizar la instalación de la librerías contenidas en el fichero requirements.txt:
```
pip3 install -r requirements.txt
```

* Deberás declarar la variable de entorno "TOKEN" con el contenido del token que te facilitaron al crear el bot.

* Para hacerlo funcionar, únicamente deberás ejecutar el siguiente comando dentro de la carpeta src:
```
python3 main.py
```

## Despliegue con Docker :whale:

* Primero construiremos la imagen que contendrá nuestro bot:
```
docker build -t discord-bot .
```

* Después levantaremos el contenedor. Al levantar el contenedor vamos a montar una carpeta del servidor de docker, que debemos especificarlo en la parte del comando donde indica "carpeta_host". La "carpeta_contenido" será la carpeta dentro del contenedor donde tengamos los ficheros:
```
docker run -dti --env TOKEN="nuestro_token" --name discord-bot-container discord-bot 
```

## Despliegue en Kubernetes :anchor:

Antes de empezar el despliegue debemos subir la imagen de Docker con el código aun Registry privado.

* Creamos el namespace en nuestro cluster:
```
kubectl create namespace discordbot
```

* Añadimos el secret con las credenciales de nuestro registry privado:
```
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword>
```

* Desplegamos el secret que contendrá el Token de nuestro bot. Antes de ejecutar el comando, recordad rellenar el campo "token":
```
kubectl apply -f secret.yaml
```

* Desplegamos nuestro bot:
```
kubectl apply -f deployment.yaml
```

## Pipelines
En la carpeta "pipelines" podeis encontrar un fichero Jenkinsfile para realizar los test de calidad, seguridad y estáticos con las siguientes librerías de Python:
* [flake8]: https://flake8.pycqa.org/en/latest/ -
* [radon]: https://pypi.org/project/radon/ -
* [bandit]: https://pypi.org/project/bandit/ -

## Librerías usadas :books:
Python:
* [youtube-dl]: https://pypi.org/project/youtube_dl/ -
* [pynacl]: https://pypi.org/project/PyNaCl/ -
* [beautifulsoup]: https://pypi.org/project/beautifulsoup4/ -
* [requests]: https://docs.python-requests.org/en/master/ - 
* [os]: https://docs.python.org/3/library/os.html -