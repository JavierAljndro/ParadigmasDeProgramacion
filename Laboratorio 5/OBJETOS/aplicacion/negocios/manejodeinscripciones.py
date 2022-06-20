 from aplicacion.modelos.usuario import Usuario
 from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

 #============================
 # Clase storemanager
 # NO TIENEN VARIABLES !!!
 #----------------------------
 class ManejoDeInscripciones:
     #==========================================================
     # Decorador staticmethod 
     # El objeto sólo tiene la función inscribirUsuario
     # ENVUELVE LA FUNCINON SIN LLAMAR VARIABLES LOCALES
     # el objeto ManejoDeInscripciones es la interface intercambiamble
     #----------------------------------------------------------------
     @staticmethod 
     def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
         print("-------> Guardando usuario... \n")
         repositorioDeUsuarios.abrir()
         repositorioDeUsuarios.guardar(usuario)
         repositorioDeUsuarios.cerrar()


