## Instructions
1. Run `docker-compose build`
2. Run `docker-compose up -d`
3. View logs by running `docker-compose logs -f`
4. Build the css in the container `./tailwindcss -i static/src/app.css -o static/dist/app.css --watch` or with `docker compose exec djangoblog ./tailwindcss -i static/src/app.css -o static/dist/app.css --watch`
5. bring down the container(s) `docker-compose down -v`