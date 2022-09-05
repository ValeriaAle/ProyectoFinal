#Proyecto Final
  Se trata de una pagina web para mi empresa familiar con años de trayectoria. 
  Desde 2018 brindamos nuestros servicios a clientes y estudios de arquitectura, ejecutando proyectos de remodelación, construcción llave en mano con o sin terreno y obras comerciales.
  
Pre - requisitos
   Tener instalado
      Visual Studio Code
      DB Browser(SQLite)
      Acceso a github

Instalación
Descargar en la maquina local los fuentes
Abrir VSC y abrir una nueva terminal
Usando los comandos "cd" llegar hasta la carpeta ProyectoFinal/ProyectoFinal
Con el comando "ls" validar que se encuentra a la altura del archivo manage.py
Con el comando "python manage.py runserver" levantar el servidor
Se muestra dos opciones "admin/" o "Constructora/" (nombre de la aplicación)
Dentro de admin/ se puede ver los usuarios creados mediante el comando createsuperuser y los registros de las tablas ficha_tecnica, casa, clientes
Dentro de esta url se ve el home de la pagina "http://127.0.0.1:8000/Constructora/" aún pelado.
Dentro de la aplicación se cargar una nueva casa (http://127.0.0.1:8000/Constructora/casaFormulario), una ficha tecnica (para obras comerciales)http://127.0.0.1:8000/Constructora/fichaFormulario
y un nuevo cliente http://127.0.0.1:8000/Constructora/clientesFormulario). 
Para buscar una ficha tecnica: http://127.0.0.1:8000/Constructora/busquedaFicha, ingresando un valor correspondiente al campo obra
Para buscar un cliente http://127.0.0.1:8000/Constructora/busquedaCliente, ingresando el nombre y apellido
Para buscar una casa http://127.0.0.1:8000/Constructora/busquedaCasa, ingresando el nro. de casa
