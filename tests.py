from datetime import datetime
from django.test import TestCase

from .models import Post

def make_dummy_post(name):
	return Post.objects.create(title=name, content="dummy")

# Create your tests here.
class PostModelTest(TestCase):
	def test_set_default_datetime(self):
		now = datetime.now()
		dummy_post = make_dummy_post("dummy")
		self.assertEqual(dummy_post.date_created.strftime("%Y-%m-%d %H:%M:%S"), now.strftime("%Y-%m-%d %H:%M:%S"))
		