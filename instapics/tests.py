from django.test import TestCase
from .models import Location,Image,Category
# Create your tests here.


class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.kigali=Location(name='Kigali')
# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
# Testing save method
    def test_save_location(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

# Testing delete method
    def test_delete_location(self):
        self.kigali.save_location()
        self.kigali.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)



class CategoryTestClass(TestCase):
    def setUp(self):
        self.food=Category(name='Food')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

# Testing save method
    def test_save_category(self):
        self.food.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.food.save_category()
        self.food.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.new_location=Location(name='kigali')
        self.new_location.save_location()

        self.new_category=Category(name='Food')
        self.new_category.save_category()

        self.new_image=Image(image_name='Test name',image_description='Test description',image_category=self.new_category,image_location=self.new_location)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)