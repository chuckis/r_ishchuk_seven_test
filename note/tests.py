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

class TestSignup(unittest.TestCase):

 def setUp(self):
     self.driver = webdriver.Firefox()

 def test_signup_fire(self):
     self.driver.get("http://localhost:8000/add/")
     self.driver.find_element_by_id('id_title').send_keys("test title")
     self.driver.find_element_by_id('id_body').send_keys("test body")
     self.driver.find_element_by_id('submit').click()
     self.assertIn("http://localhost:8000/", self.driver.current_url)

 def tearDown(self):
     self.driver.quit

if __name__ == '__main__':
 unittest.main()

# api

#from tastypie.test import ResourceTestCase

#class EntryResourceTest(ResourceTestCase):

    #def test_get_api_json(self):
        #resp = self.api_client.get('/api/note/', format='json')
        #self.assertValidJSONResponse(resp)

    #def test_get_api_xml(self):
        #resp = self.api_client.get('/api/note/', format='xml')
        #self.assertValidXMLResponse(resp)

# model mommy

from model_mommy import mommy

class WhateverTestMommy(TestCase):

    def test_whatever_creation_mommy(self):
        n = mommy.make(Note)
        self.assertTrue(isinstance(n, Note))
        self.assertEqual(n.__unicode__(), n.title)

