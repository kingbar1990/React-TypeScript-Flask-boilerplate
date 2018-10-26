

### Build project

1. Rename ".env.example" to ".env"
```bash
mv .env.example .env
```
2. Create files folder
```bash
mkdir server/files
```

3. Build docker-compose
```bash
docker-compose build
```

4. Create database
```bash
docker-compose up -d database
```

5. Make database migrations
```bash
docker-compose run flask python manage.py db upgrade
```

6. Create mode_modules
```bash
docker-compose run node yarn
```

7. Run the project
```bash
docker-compose up
```

8. Open in your browser http://localhost:3000/

### Run tests

```bash
docker-compose run flask pytest
```
