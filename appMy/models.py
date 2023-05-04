from django.db import models

# Create your models here.

    
class Header(models.Model):
     header_img=models.ImageField(("Header-fotoğrafı"), upload_to="images/",)
     company_head=models.CharField("Başlık",max_length=100,null=True)
     company_name=models.CharField("Şirket adı",max_length=100)
     company_subtitle=models.CharField("Alt yazı",max_length=100,null=True)

class Welcome(models.Model):
    text=models.TextField((""),null=True)
    text_card_img=models.ImageField(("Fotoğraf yükle"), upload_to='images/',null=True,blank=True)
    class Meta:
        verbose_name_plural = "Hoş Geldin"
        
        def __str__(self) -> str:
            return self.title
        
        
class Card(models.Model):
    image=models.ImageField((""), upload_to="images/",null=True)
    text_head=models.CharField(("Başlık"), max_length=50)
    text=models.TextField(("Alt yazı"))



class detailCard(models.Model):
    detail_card_icon= models.CharField("icon",max_length=100)
    detail_title=models.CharField("baslık",max_length=100)
    detail_title_card=models.CharField("kart baslık",max_length=100,null=True)
    detail_text=models.TextField("")
    
class Cardtwo(models.Model):
    image=models.ImageField((""), upload_to="images/",null=True)
    text_head=models.CharField(("Başlık"), max_length=50)
    text=models.TextField(("Alt yazı"))
    
    
class latestNews(models.Model):
    news_img=models.ImageField(("Fotoğraf"), upload_to="images/",null=True)
    news_text=models.TextField((""))
    news_date=models.DateField(("Tarih"), auto_now=False, auto_now_add=False)
    news_img_text=models.TextField(("Fotoğraf alt yazı"))
    
    
class Team(models.Model):
    team_img=models.ImageField(("profil fotoğrafı"), upload_to="images/")
    team_name=models.CharField(("ad/soyad"), max_length=50)
    team_comment=models.TextField((""))
    class Meta:
        verbose_name_plural = "Kadro"
