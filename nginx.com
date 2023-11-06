worker_processes auto:

events{
}

http{
  server {
    listen 80;

    location / {
        proxy_pass http://django_container_gunicorn:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
}