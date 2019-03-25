from django.db import models


class Location(models.Model):
  place = models.CharField(max_length=30)

  def __str__(self):
      return self.place

  class Meta:
      ordering = ['place']

  def save_location(self):
      self.save()




class Category(models.Model):
  category = models.CharField(max_length=30)

  def __str__(self):
      return self.category

  def save_category(self):
      self.save()


class Image(models.Model):
  image = models.ImageField(upload_to='gallery/')
  image_name = models.CharField(max_length=25)
  image_description = models.TextField(max_length=300)
  image_location = models.ForeignKey(Location)
  image_category = models.ForeignKey(Category)



  def __str__(self):
      return self.image_name


  def save_image(self):
      self.save()

  def delete_image(self):
      self.remove()

  def update_image(self, id):
      pass

  def get_image_by_id(id):
      pass

  def search_image(image_category):
      pass

  def filter_by_location(image_location):
      pass

  @classmethod
  def search_by_category(cls,search_term):
        photos=cls.objects.filter(image_category__category__contains=search_term)
        return photos

  @classmethod
  def get_one_image(cls,id):
        try:
            image=Image.objects.get(id=id)
            return image
        except DoesNotExist:
            return Image.objects.get(id=1) 

  @classmethod
  def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images  

