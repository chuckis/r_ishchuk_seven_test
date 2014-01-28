from django.test import TestCase
from note.models import Note
from django.utils import timezone
from django.core.urlresolvers import reverse


# models test

class NoteTest(TestCase):

    def create_note(self, title="only a test", body="yes, this is only a test"):
        return Note.objects.create(title=title, body=body, created_at=timezone.now())

    def test_note_creation(self):
        n = self.create_note()
        self.assertTrue(isinstance(n, Note))
        self.assertEqual(n.__unicode__(), n.title)


# views (uses reverse)

def test_note_list_view(self):
    n = self.create_note()
    url = reverse("note.views.note")
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)
    self.assertIn(n.title, resp.content)

# forms

# views (uses selenium)

import unittest
from selenium import webdriver

if __name__ == '__main__':
 unittest.main()

# model mommy

from model_mommy import mommy

class NoteTestMommy(TestCase):

    def test_note_creation_mommy(self):
        n = mommy.make(Note)
        self.assertTrue(isinstance(n, Note))
        self.assertEqual(n.__unicode__(), n.title)

