from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='admin@email.com', password='admin1234')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='test@email.com', password='test1234', name='full name')

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(response=res, text=self.user.name)
        self.assertContains(response=res, text=self.user.email)

    def test_user_change_page(self):
        """Test that user edit page wordks"""

        url = reverse('admin:core_user_change', args=[self.user.id])  # /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
