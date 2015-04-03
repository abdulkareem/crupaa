from django.db import models
from django import forms
from image_cropping import ImageRatioField, ImageCropField


# Create your models here.
class Categorie(models.Model):
    titolo = models.CharField("Titolo:", max_length=100)
    titolo_fr = models.CharField("Titolo Francese:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)

    def __unicode__(self):
		return self.titolo



class Aziende(models.Model):
    denominazione = models.CharField("Denominazione:", max_length=100)
    email = models.CharField("E-mail:", max_length=100, blank=True, null=True)
    telefono = models.CharField("Telefono:", max_length=100, blank=True, null=True)
    Fax = models.CharField("Fax:", max_length=100, blank=True, null=True)
    web = models.CharField("Sito Web:", max_length=100, blank=True, null=True)
    nazione = models.CharField("Nazione:", max_length=100, blank=True, null=True)
    indirizzo = models.CharField("indirizzo:", max_length=100, blank=True, null=True)
    titolo = models.CharField("cap:", max_length=100, blank=True, null=True)
    citta = models.CharField("citta:", max_length=100, blank=True, null=True)
    piva = models.CharField("Piva:", max_length=100, blank=True, null=True)
    codfisc = models.CharField("CodiceFiscale:", max_length=100, blank=True, null=True)

    def __unicode__(self):
		return self.titolo
    class Meta:
		verbose_name_plural = "Partner Aziende/Marchi Commerciati"


class Immagini(models.Model):
	titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
	didascalia = models.TextField(null=True, blank=True)
	cropping = ImageRatioField('image', '500x480')
	slidepage = ImageRatioField('image', '870x480')
	croppingthumb = ImageRatioField('image', '600x450')
	croppingslide = ImageRatioField('image', '1140x487')
	croppingcarousel = ImageRatioField('image', '198x132')
	freecropping = ImageRatioField('image', '1200x1125', free_crop=True, verbose_name="Freecropping")
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo
	class Meta:
		verbose_name_plural = "Galleria Immagini"
        ordering = ['id']



class Prodotti(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_fr = models.CharField("Titolo Francese:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categorie, null=True, blank=True)
    marchio = models.ForeignKey(Aziende, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_fr = models.TextField(null=True, blank=True, verbose_name="Descrizione Francese")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    croppingminiatura = ImageRatioField('image', '500x469', verbose_name="Miniatura")
    croppingslider = ImageRatioField('image', '500x469', verbose_name="Slider Revolution")
    cropping = ImageRatioField('image', '500x469', verbose_name="Cropping")
    croppingfree = ImageRatioField('image', '500x469', free_crop=True, verbose_name="Free Crop")
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    video = models.CharField("Video:", max_length=100, null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo


class Page(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_fr = models.CharField("Titolo Francese:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_fr = models.TextField(null=True, blank=True, verbose_name="Descrizione Francese")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    croppingminiatura = ImageRatioField('image', '500x469', verbose_name="Miniatura")
    croppingslider = ImageRatioField('image', '500x469', verbose_name="Slider Revolution")
    cropping = ImageRatioField('image', '500x469', verbose_name="Cropping")
    croppingfree = ImageRatioField('image', '500x469', free_crop=True, verbose_name="Free Crop")
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    video = models.CharField("Video:", max_length=100, null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo


class Slider(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
    titolo_fr = models.CharField("Titolo Francese:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    active = models.BooleanField(default=False)
    didascalia = models.TextField(null=True, blank=True)
    didascalia_fr = models.TextField(null=True, blank=True, verbose_name="Didascalia Francese")
    didascalia_uk = models.TextField(null=True, blank=True, verbose_name="Didascalia Inglese")
    cropping = ImageRatioField('image', '1170x500')
    slidepage = ImageRatioField('image', '870x480')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
		return self.titolo
    class Meta:
		verbose_name_plural = "Slider in Homepage"
        #ordering = ['id']


#### FORM CONTATTI
class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cognome = forms.CharField(label='Cognome', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=100, required = False)
    fax = forms.CharField(label='Fax', max_length=100, required = False)
    email = forms.CharField(label='email', max_length=100)
    citta = forms.CharField(label='Citta', max_length=100, required = False)
    indirizzo = forms.CharField(label='Indirizzo', max_length=100, required = False)
    messaggio = forms.CharField(label='Messaggio', widget=forms.Textarea, required = False)