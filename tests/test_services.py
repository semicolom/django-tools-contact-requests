from django.test import TestCase
from djtools.contactrequests import services
from djtools.contactrequests.models import ContactRequest


class ServicesTestCase(TestCase):
    def test_send_mail(self):
        contact_request = ContactRequest.objects.create()
        amount_sent_emails = services._send_mail(contact_request)
        self.assertEqual(amount_sent_emails, 1)

    def test_create_contact_request(self):
        contact_request, amount_sent_emails = services.create_contact_request(
            name="test",
            email="test@example.com",
            phone_number="555-123",
            message="Test"
        )
        self.assertEqual(contact_request.name, "test")
        self.assertEqual(amount_sent_emails, 1)
