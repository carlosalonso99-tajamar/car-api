# Usa una imagen base ligera con Python
FROM python:3.9-slim

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto donde correrá la aplicación
EXPOSE 5000

# Usa Gunicorn como servidor WSGI
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
