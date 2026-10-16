from django.db import models


class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    ficha = models.CharField(max_length=20)
    lugar = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField()
    modalidad = models.CharField(max_length=50)
    nivel_profesion = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.ficha}"


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=24)
    ficha_asignada = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="instructores"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=24, unique=True)
    correo = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=24)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.PROTECT,
        related_name="aprendices"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    ficha = models.CharField(max_length=20)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="competencias"
    )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="competencias"
    )

    def __str__(self):
        return self.nombre