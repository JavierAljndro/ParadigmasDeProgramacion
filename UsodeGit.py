#=====================================#
#   Subir archivos a GitHub con Git   #
#=====================================#

Primero tenémos que crear nuestro repositorio directamente
desde la página de GitHub.
Mi recomendación es no agregarle el archivo "README", ya que
al momento de crearlo vendrán unos códigos que serán de ayuda
después.


# Por ejemplo:
'Para crear un nuevo repositorio'
#------------------------------------------------------------------------
echo "# Repositorio" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Repositorio/Repositorio.git
git push -u origin main
#------------------------------------------------------------------------


'Insertar un repositorio existente'
#------------------------------------------------------------------------
git remote add origin https://github.com/Repositorio/Repositorio.git
git branch -M main
git push -u origin main
#------------------------------------------------------------------------


En este caso, será con un repositorio ya existente:

  ° Nos colocamos en nuestro proyecto (repositorio ó carpeta en nuestra máquina
    y ponemos el comando
    # git init
    para inicializar github de forma local en nuestro repositorio


  ° Hacemos # git status
   para ver saber qué archivos están modificados

  ° Agregamos archivos con #git add "nombre del archivo"
    ''' ó en su defecto, pueden agregárse todos de golpe con
    # git add . '''

  ° Luego # git commit -m "MENSAJE" 
    para agregar una descripción al archivo
  
  ° Ahora los archivos se habrán subido a Git de forma LOCAL,
    (o sea, en la computadora).
    Para subir esos archivos de Git local al GitHub online
    usamos el código que nos aparece al principio:
    # git remote add origin https://github.com/Repositorio/Repositorio.git

  ° Luego creamos nuestra rama principal
    # git branch -M main

  ° Y por último hacemos un push (empujamos) nuestros programas locales a Github
    con el siguiente comando (el que venía al inicio)
    # git push -u origin main


###################################################################
# NOTA: la contraseña es un token que se genera por cierto tiempo #
###################################################################

