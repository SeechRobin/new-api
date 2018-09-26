from django.test import TestCase

from .models import News , Comments

class ModelTestCase(TestCase):
    """This class defines the test suite for the news  model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.newslist_name = "Write world class code"
        self.newslist = News(name=self.newslist_name)
        self.client = APIClient()
        self.newslist_data = {'title': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.newslist_data,
            format="json")

    def test_model_can_create_a_news(self):
        """Test the newslist model can create a newslist."""
        old_count = News.objects.count()
        self.newslist.save()
        new_count = News.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_create_a_news(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_news(self):
        """Test the api can get a given news article."""
        newslist = News.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': news.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, newslist)

    def test_api_can_update_news(self):
        """Test the api can update a given newslist."""
        change_newslist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': newslist.id}),
            change_newslist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_news(self):
        """Test the api can delete a newslist."""
        newslist = News.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': newslist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
