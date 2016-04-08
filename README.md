# Rest_Api_social_H4ck

Simple rest api creada en python con framework django

## Instalación y configuración

#### Descarga el codigo
  ```bash
    $ git clone https://github.com/jomarquez21/Rest_Api_social_H4ck.git
  ```

#### Entra en el proyecto

  ```bash
    $ cd Rest_Api_social_H4ck
  ```

#### Instala las liberias requeridas

  ```bash
    $ pip install -r requirement.txt
  ```
  
#### Ejecuta la migración

  ```bash
    $ python manage.py migrate
  ```
  
#### Ejecuta el servidor

  ```bash
    $ python manage.py runserver
  ```
  
## Rutas del proyecto
  
#### Para crear un usuario
  
  Debe hacer una peticion post a la siguiente url
  
  [http://127.0.0.1:8000/user/](http://127.0.0.1:8000/user/)
  
#### Para editar un usuario

  Debe hacer una peticion put a la siguiente url
  
  [http://127.0.0.1:8000/user/<id_user>/](http://127.0.0.1:8000/user/<id_user>/)
  
#### Para lista un usuario

  Debe hacer una peticion get a la siguiente url
  
  [http://127.0.0.1:8000/user/<id_user>/](http://127.0.0.1:8000/user/<id_user>/)

#### Para elimiar un usuario

  Debe hacer una peticion delete a la siguiente url
  
  [http://127.0.0.1:8000/user/<id_user>/](http://127.0.0.1:8000/user/<id_user>/)

#### Para listar todos los usuarios

  Debe hacer una peticion get a la siguiente url
  
  [http://127.0.0.1:8000/user/all/](http://127.0.0.1:8000/user/all/)
  
  Los parametro get para la busqueda
  
  * name (name)<br>
  * gender (genero)<br>
  * email (email)<br>
  * page_results (total de resultados por pagina)<br>
  * page_index (pagina index en paginado)<br>
