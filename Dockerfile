#imagen python.
FROM python:3.9

#Copia el directorio del contenedor.
COPY . /SQL_ALCHEMY
WORKDIR /SQL_ALCHEMY
RUN pip install -r requirements.txt

#expone el puerto del contenedor
EXPOSE 5005

ENTRYPOINT ["python3"]
CMD ["app/__init__.py"]