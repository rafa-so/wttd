# coding: utf-8
from django.test import TestCase

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ must return status code'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_form.html')

    def test_html(self):
        'Html must contain input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token'
        self.assertContains(self.resp, csrfmiddlewaretoken)
