from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_homepage(self):
        # Создаем экземпляр клиента
        guest_client = Client()
        # создаем запрос к главной странице
        response = guest_client.get('/')
        # утверждаем что должен быть статус 200
        self.assertEquals(response.status_code, 200)
