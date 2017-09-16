from django.test import TestCase


class GentelellaUrlsTest(TestCase):
    def test_index(self):
        resp = self.client.get('/gentelella/index.html')
        self.assertEqual(200, resp.status_code)

    def test_other(self):
        resp = self.client.get('/gentelella/tables.html')
        self.assertEqual(200, resp.status_code)
