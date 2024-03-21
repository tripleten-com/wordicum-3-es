# Wordicum-3

## CCreación de un repositorio
1. Crea un repositorio para ti utilizando esta plantilla.
  Presiona el botón "Use this template" (Usar esta plantilla) y selecciona la opción "Create a new repository" (Crear un nuevo repositorio).
  ![image](https://user-images.githubusercontent.com/14962819/235599080-2819c72b-3161-48fe-926d-91c289941c20.png)
  
2. Rellena los campos **Repository name** (Nombre del repositorio) y **Description** (Descripción) y haz clic en el botón "Create repository from template" (Crear repositorio a partir de una plantilla).
  ![image](https://github.com/tripleten-com/Wordicum-3/assets/120686503/029f2e5a-2718-4d34-90ed-e673c218e7ec)

## Cómo trabajar con el repositorio
Para empezar la tarea, necesitas copiar la URL de tu repositorio y clonarlo. Ten en cuenta que estás clonando tu propio repositorio, ¡no la plantilla original!
  ![image](https://github.com/tripleten-com/Wordicum-3/assets/120686503/b4e31f6c-8e34-4d7f-8b5a-18c3f776ac21)
  
### Creación de un entorno virtual

1. Inicia el editor Visual Studio Code y, a través del menú "*Archivo"/"Abrir directorio"*, abre la carpeta *Dev/wordicum-3/*.
2. Inicia la terminal en VS Code y asegúrate de trabajar desde el directorio *wordicum-3/*. Si utilizas Windows, asegúrate de que Git Bash se ejecute en la terminal y no a través de otra herramienta, como PowerShell. Ejecuta este comando:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
El entorno virtual se desplegará en el directorio *wordicum-3/*. La carpeta `venv` también aparecerá allí, y almacenará todas las dependencias del proyecto. La estructura del archivo se vera así:

```
Dev/
 └── wordicum-3/
     ├── tests/             Pruebas de TripleTen para el proyecto
     ├── venv/              Directorio del entorno virtual
     ├── wordicum-3/         <-- Directorio del proyecto
     |   ├── ...            <-- Estructura del proyecto de Django
     |   └── manage.py      
     ├── .gitignore         Lista de archivos y carpetas que no se pueden rastrear con Git
     ├── db.json            <-- Fixtures para la base de datos
     ├── LICENSE            Licencia  
     ├── pytest.ini         Configuración de las pruebas de TripleTen
     ├── README.md          Descripción del proyecto
     └── requirements.txt   Lista de dependencias del proyecto
```

### Activación del entorno virtual
En la terminal, navega hasta el directorio raíz del proyecto *Dev/wordicum-3/* y ejecuta este comando:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Ahora todos los comandos en la terminal irán precedidos por el string `(venv)`.

💡 Todos los comandos posteriores en la terminal deben ejecutarse con el entorno virtual activado.

Actualiza pip:

```bash
python -m pip install --upgrade pip
```

### Instalar las dependencias del archivo *requirements.txt*
Mientras estás en la carpeta *Dev/wordicum-3/*, ejecuta este comando:

```bash
pip install -r requirements.txt
```

#### Fin del soporte de dependencias

Se seleccionaron las versiones LTS de las dependencias.
Para Django, se seleccionó la versión 3.2.Su soporte extendido
[finaliza](https://endoflife.date/django) el 1 de abril de 2024.

### Usar migraciones


En el directorio con el archivo "manage.py", ejecuta el siguiente comando:

```bash
python manage.py migrate
```

### Ejecutar el proyecto en modo dev


En el directorio con el archivo "manage.py", ejecuta el siguiente comando:

```bash
python manage.py runserver
```

En respuesta, Django indicará que el servidor está funcionando y que el proyecto está disponible en la dirección  [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Inicio de pruebas locales
Cuando hayas terminado la tarea, inicia las pruebas locales. En la terminal, navega hasta el directorio raíz del proyecto *Dev/wordicum-3/* y ejecuta este comando:
```shell
pytest
```
Si todos los casos de prueba tienen éxito, el proyecto se considerará completado. De lo contrario, tendrás que corregir las partes que no han pasado las pruebas e iniciarlas de nuevo.
