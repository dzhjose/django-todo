# django-todo
Todo app with Django and Tailwindcss

# Create virtual enviroment
- python -m venv {name of virutal enviroment i always use 'venv'}

# Activate virtual enviroment
- Linux
  - source venv/bin/activate
- Windows
  - source venv\Scripts\activate
  
# Install requirements with pip
- pip install -r requirements.txt
- run ./manage.py collectstatic -> this will move all the static files to staticfiles folder, this will load the necessary assets for the app

# After installations
- migrate the models
  - ./manage.py makemigrations -> this will crate the migrations for the apps in apps folder
  - ./manage.py migrate

# Install tailwindcss
- cd tw/
- npm install
- npm run dev

# End
- after do all the instructions run ./manage.py runserver and go to localhost:8000 to see the result
- ***Importat:*** you must quit running npm run dev for development or npm run build, this will add all the css rules you ad in the templates and will added for the css file in static folder
