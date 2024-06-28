## Instalación en un entorno virtual
Instalación sobre Linux. Deberá proveer una base de datos postgres o cambiar la configuración en settings.py para adecuala a la base da datos que use.

```bash
git clone https://github.com/VulturARG/challenger_N5.git
cd challenger_N5
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env # Completar los datos si se requiere
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

## Ejecución en puerto 8000
```bash
python3 manage.py runserver 0.0.0.0:8000
```

## Test automáticos
### Correr test
```bash
python3 coverage run manage.py test
```

### Correr coverage
```bash
coverage run manage.py test
```

### General reporte HTML
```bash
coverage html
```