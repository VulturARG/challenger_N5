## Instalación en un entorno con docker
Para el desarrollo del sistema se ha implementado sobre docker con Python 3.8 de acuerdo a los requerimientos.

```bash
git clone https://github.com/VulturARG/challenger_N5.git
cd challenger_N5
docker-compose build
cp .env.example .env # Completar los datos si se requiere
docker-compose run --rm web python3 manage.py makemigrations
docker-compose run --rm web python3 manage.py migrate
docker-compose run --rm web python3 manage.py createsuperuser
```

## Inicio y parada

```bash
docker-compose up -d
docker-compose stop
```

## Remover contenedores

```bash
docker-compose down
```

## Test automáticos
### Correr test
```bash
docker-compose run --rm web python coverage run manage.py test
```

### Correr coverage
```bash
docker-compose run --rm web coverage run manage.py test
```

### General reporte HTML
```bash
docker-compose run --rm web coverage html
```