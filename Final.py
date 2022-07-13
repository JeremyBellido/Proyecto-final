cabecera=['NOMBRE','APELLIDO','CATEGORIA','HORAS','PAGA NETA','PAGA BRUTA']
trabajadores={}

catMOD=''
cataMOD=0
totalMOD=0
catbMOD=0
opcion='*'
while opcion.lower() !='0':
    print('\nINICIO:')
    print('{0:^44}'.format('_'*41))
    print('{1}{0:^41}{1}'.format('Menú de opciones','|'))
    print('{1}{0}{1}'.format('_'*41,'|'))
    print('{2}{0:^30}{2}{1:^10}{2}'.format('','Opciones','|'))
    print('{2}{0:^30}{2}{1:^10}{2}'.format('','','|'))
    print('{2}{0:^30}{2}{1:^10}{2}'.format('Registrar trabajador','---->(1)','|'))
    print('{2}{0:^30}{2}{1:^10}{2}'.format('Imprimir lista de trabajadores','---->(2)','|'))
    print('{2}{0:^30}{2}{1:^10}{2}'.format('Salir','---->(0)','|'))
    print('{1}{0}{1}'.format('_'*41,'|'))
    opcion = input('\nElija una opción: ')
    if opcion.lower()=='1':
        import a
        a.trabaja(cabecera,trabajadores,cataMOD,catbMOD,totalMOD,catMOD)
    elif opcion.lower()=='2':
        import a
        a.listado(cabecera,trabajadores,cataMOD,catbMOD,totalMOD,catMOD)
    else:
        print('ERROR\nNo encontramos la opcion.\nVuelvalo a intentar')
