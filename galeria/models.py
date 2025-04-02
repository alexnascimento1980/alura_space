from django.db import models

class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("GALAXIA", "Galáxia"),
        ("ESTRELA", "Estrela"),
        ("PLANETA", "Planeta"),        
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
