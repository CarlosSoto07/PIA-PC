# PIA-PC
En este repositorio se encuentra el proyecto final de la materia Programación de Ciberseguridad

## Requisitos
_tener la version actualizada de python 3.9_
_instalar los modulos externos de python ejecutando el requirements.txt_
pip install -r requierements.txt


## Herramientas de Ciberseguridad

_webscrapping: solo ingresar -w_

_correos: ingresar -c y llenar input de destinatario ,asunto y contraseña de remitente_

_dns: ingresar -d y la ip deseada a analizar (puerta de enlace predeterminada)_
example: py main.py -d 192.168.100.1

_hunter: -k para ingresar apikey de hunter_
         _-t archivo txt con los correos a buscar_
example: py main.py -k 7423f7ac035e69bd7552283469acf1f4f4bdd564 -t correosHunter.py

_metadatos: -m ingresar la ruta de la carpeta con los archivos .pdf y .jpg_
example: py main.py  C:\Users\carlo\Desktop\PC\PIA\Metadata

_zip: -z comprime en un archivo .zip todos los archivos necesarios para el PIA_

## Integrantes 
-Carlos Adrián Soto Serna
-Jose Humberto Martinez Peña
-Luis Julian Ramos Castañeda
-Andrea Paola Arzate Rodriguez
-Gerson Emannuel Reyes Contreras
