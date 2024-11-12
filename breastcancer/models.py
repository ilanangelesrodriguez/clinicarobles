from django.db import models

# Create your models here.

class Paciente(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]

    dni = models.CharField(max_length=8, unique=True)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        default=MASCULINO,
    )
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    algoritmo = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    descripcion = models.TextField()
    fecha_implementacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} (v{self.version})"

class Zona(models.Model):
    DIAGNOSIS_CHOICES = [
        ('B', 'Benigno'),
        ('M', 'Maligno'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    diagnosis = models.CharField(
        max_length=1,
        choices=DIAGNOSIS_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Zona {self.ubicacion} de {self.paciente}"

class Examen(models.Model):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    fecha = models.DateField()
    # Campos de medidas
    radius_mean = models.FloatField()
    texture_mean = models.FloatField()
    perimeter_mean = models.FloatField()
    area_mean = models.FloatField()
    smoothness_mean = models.FloatField()
    compactness_mean = models.FloatField()
    concavity_mean = models.FloatField()
    concave_points_mean = models.FloatField()
    symmetry_mean = models.FloatField()
    fractal_dimension_mean = models.FloatField()
    radius_se = models.FloatField()
    texture_se = models.FloatField()
    perimeter_se = models.FloatField()
    area_se = models.FloatField()
    smoothness_se = models.FloatField()
    compactness_se = models.FloatField()
    concavity_se = models.FloatField()
    concave_points_se = models.FloatField()
    symmetry_se = models.FloatField()
    fractal_dimension_se = models.FloatField()
    radius_worst = models.FloatField()
    texture_worst = models.FloatField()
    perimeter_worst = models.FloatField()
    area_worst = models.FloatField()
    smoothness_worst = models.FloatField()
    compactness_worst = models.FloatField()
    concavity_worst = models.FloatField()
    concave_points_worst = models.FloatField()
    symmetry_worst = models.FloatField()
    fractal_dimension_worst = models.FloatField()

    def __str__(self):
        return f"Examen de {self.zona} el {self.fecha}"

    class Meta:
        verbose_name_plural = "Exámenes"

class Prediccion(models.Model):
    DIAGNOSIS_CHOICES = [
        ('B', 'Benigno'),
        ('M', 'Maligno'),
    ]

    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name="predicciones")
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=1, choices=DIAGNOSIS_CHOICES)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Predicción {self.prediction} para {self.examen} con {self.modelo}"

    class Meta:
        verbose_name_plural = "Predicciones"
