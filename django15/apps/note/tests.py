from django.test import TestCase
from django15.apps.note.models import Note
from django.utils import timezone
from django.core.urlresolvers import reverse
from model_mommy import mommy

# models test

class NoteTest(TestCase):
    """
    tests...
    """
    def create_note(self, title="only a test", body="yes, this is only a test"):
        return Note.objects.create(title=title, body=body, created_at=timezone.now())

    def test_note_creation(self):
        n = self.create_note()
        self.assertTrue(isinstance(n, Note))
        self.assertEqual(n.__unicode__(), n.title)

# views (uses reverse)

    def test_note_list_view(self):
        n = self.create_note()
        url = reverse("note-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(n.title, resp.content)

if __name__ == '__main__':
 unittest.main()

# model mommy

class NoteTestMommy(TestCase):

    def test_note_creation_mommy(self):
        n = mommy.make(Note)
        self.assertTrue(isinstance(n, Note))
        self.assertEqual(n.__unicode__(), n.title)

