#Miprimerpagina
Proyecto desarollado con Django, siguiendo el patron MTV
#Estructura
Modelos: autor, categoria, post.
Herencia de PL: todos los templates se extienden de "base html".
Formularios: forms.py para cada Modelo.
Formulario de busqueda: busca posts por titulo.
#Funcionalidades:
inicio:
- Ruta: `/`
- Página principal del blog
crear autor:
- Ruta: `/crear_autor/`
- Formulario para crear un autor
crear categoria:
- Ruta: `/crear_categoria/`
- Formulario para crear una categoría
crear post:
- Ruta: `/crear_post/`
- Formulario para crear un post con autor y categoría
buscar post:
- Ruta: `/buscar_post/`
- Formulario de búsqueda por título de post
#requisitos:
- Python 3.x
- Django 5.x
- Ejecutar `py manage.py migrate` antes de iniciar el servidor
en bash:
py manage.py runserver
En tu navegador:
Abrí http://127.0.0.1:8000 en el navegador.
