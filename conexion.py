import mysql.connector 
conexion = mysql.connector.connect (user= 'ValentinoCe', 
                                    password = 'V@lentino*45740280',
                                    host ='localhost',
                                    database= 'resgistro_usuario',
                                    port = '3306')
print (conexion)

