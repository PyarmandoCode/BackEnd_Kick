Proceso PromedioNotas
	Definir nota,suma,contador Como Real
	suma<-0 //Inicializar las notas en cero
	contador<-0 //Inicializar las notas en cero
	Escribir "Ingrese una nota (numero negatico para terminar)"
	Leer nota
	Mientras  nota >=0 Hacer
		suma <-suma+nota //Este es un acumulador que va a sumar todas notas ingresadas
		contador <-contador+1 //Este es un contador que realiza el conteo de  notas
		Escribir "Ingrese otra nota (negativa para terminar)"
		Leer  nota
	FinMientras
	Si contador>0 Entonces
		Escribir "El promedio es:" ,suma / contador
	SiNo
		Escribir "No se Ingresaron Notas Validas"
	FinSi
FinProceso
