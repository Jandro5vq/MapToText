# MapToText
PNG Map to text array, developed for a Tower Defence game map making.

=== INSTRUCTIONS ===

1. Modify "map.png" (I use Paint.NET):
	You can modify the size of the file, in my case it is 29px x 17px.
	Important to keep the colors for each type of Tile:
		- Path ---------> RGB(255, 255, 255)
		- Start Path --> RGB(0, 255, 33)
		- End Path ---> RGB(255, 0, 0, 0)
		- Water -----------> RGB(0, 38, 255)
		- Empty "Grass" -> RGB(0, 0, 0, 0)

2. Execute the file "MapToText.exe":
	It will process the image and display two windows when finished:
		1. The path painting with a gradient from purple (Start) to red (End).
		2. The corners marked with purple.

	Once you have checked that everything is OK, press any key to close.

3. The program will have created two files with the results "Map.txt" and "MapCorners.txt".


=== INSTRUCCIONES ===

1. Modificar "map.png" (yo uso Paint.NET):
	Se puede modificar el tamaño del archivo, en mi caso es 29px x 17px.
	Importante mantener los colores para cada tipo de Tile:
		- Camino ---------> RGB(255, 255, 255)
		- Inicio Camino --> RGB(0, 255, 33)
		- Final Camino ---> RGB(255, 0, 0)
		- Agua -----------> RGB(0, 38, 255)
		- Vacío "Hierba" -> RGB(0, 0, 0)

2. Ejecutar el archivo "MapToText.exe":
	Procesará la imagen y mostrara dos ventanas al finalizar:
		1. El camino pintando con un gradiente de morado (Inicio) a rojo (Fin).
		2. Las esquinas marcadas de morado.

	Una vez comprobado que todo esta bien, pulsar cualquier tecla para cerrar.

3. El programa habrá creado dos archivos con los resultados "Map.txt" y "MapCorners.txt"
