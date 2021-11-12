import zipfile
import logging

def crearZip():
	logging.info("Creacion de Archivo .Zip Iniciado..")
	
	comprimir = zipfile.ZIP_DEFLATED

	zf = zipfile.ZipFile("PIA.zip", mode="w")

	try:
	    zf.write("main.py", compress_type=comprimir)
	    zf.write("hunter.py", compress_type=comprimir)
	    zf.write("correos.py",compress_type=comprimir)
	    zf.write("correosHunter.txt", compress_type=comprimir)
	    zf.write("webScrapping.py", compress_type=comprimir)
	    zf.write("metadatos.py", compress_type=comprimir)
	    zf.write("dns.ps1", compress_type=comprimir)
	    zf.write("zip.py", compress_type=comprimir)

	finally:
	    zf.close()

	logging.info("Creacion de Archivo .Zip Finalizado..")
