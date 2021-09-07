def Seleccion(estudiantes=dict):
    promedios =[]
    MayorPromedio = 0
    for estudiante in estudiantes:
        sumatorianotas = 0
        sumatoriacreditos = 0
        for materia in estudiantes[estudiante]["materias"]:
            if materia["retirada"] != "Si":
                sumatorianotas += (materia["nota"]*materia["creditos"])
                sumatoriacreditos += materia["creditos"]  
            if sumatoriacreditos != 0:  
                promedio_ponderado = sumatorianotas/sumatoriacreditos
        promedios.append((promedio_ponderado,estudiante))
        MayorPromedio = promedios[0][0]
        PersonaGanadora = promedios[0][1]
    for NotaPersona in promedios:
        if NotaPersona[0] > MayorPromedio and NotaPersona[0]!=MayorPromedio:
            MayorPromedio = NotaPersona[0]
            PersonaGanadora = NotaPersona[1]
        if NotaPersona[0] == MayorPromedio:
            PersonaGanadora = min(NotaPersona[1],PersonaGanadora)
    nombre = estudiantes[PersonaGanadora]["nombres"]
    nombre = nombre.split()
    apellidos = estudiantes[PersonaGanadora]["apellidos"]
    apellidos = apellidos.strip()
    apellidos = apellidos.split(",")
    ultimosdigitos = (estudiantes[PersonaGanadora]["documento"])%100

    if len(nombre) == 2:
        correo = nombre[0][0]+nombre[1][0]+"."+apellidos[0].strip()+str(ultimosdigitos)
    if len(nombre) == 1:
        correo =nombre[0][0]+apellidos[0][0]+"."+apellidos[1].strip()+str(ultimosdigitos)
    
    correo = correo.lower()

    def normalize(s):
        replacements = ( ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"),("ú", "u"),)
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    correo=normalize(correo)
    codigo = PersonaGanadora
    nombres = estudiantes[PersonaGanadora]["nombres"]
    apellidos = estudiantes[PersonaGanadora]["apellidos"]
    documento = estudiantes[PersonaGanadora]["documento"]
    programa = estudiantes[PersonaGanadora]["programa"]
    promedio = MayorPromedio
    

    return ([codigo,nombres,apellidos,documento,programa,MayorPromedio,correo])