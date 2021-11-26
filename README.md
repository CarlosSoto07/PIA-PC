# PIA-PC
En este repositorio se encuentra el proyecto final de la materia Programación de Ciberseguridad

## Requisitos
_tener la version actualizada de python 3.9_

_instalar los modulos externos de python ejecutando el requirements.txt_

pip install -r requierements.txt


## Herramientas de Ciberseguridad


### webscrapping:
solo ingresar -w para que inicie la descarga de imagenes de un sitio web y la creacion de su carpeta


### correos: 
ingresar -c y llenar input de destinatario ,asunto y contraseña de remitente


### dns: 
ingresar -d y la ip deseada a analizar (puerta de enlace predeterminada)_
_example: py main.py -d 192.168.100.1_


### hunter: 
-k para ingresar apikey de hunter 

-t archivo txt con los correos a buscar

_example: py main.py -k 7423f7ac035e69bd7552283469acf1f4f4bdd564 -t correosHunter.py_


### metadatos: 
-m ingresar la ruta de la carpeta con los archivos .pdf y .jpg

_example: py main.py  C:\Users\carlo\Desktop\PC\PIA\Metadata_


### vTotal: 
-a Solicita la apikey del sitio VirusTotal para poder realizar el analisis de las urls

-tv Ingresar el nombre del archivo con las urls a analizar

_example: py main.py -a key VirusTotal -tv urls.txt_


## Integrantes 
Carlos Adrián Soto Serna

Jose Humberto Martinez Peña

Luis Julian Ramos Castañeda

