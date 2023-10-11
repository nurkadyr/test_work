from django.test import TestCase

from app.models import Log


# Create your tests here.
class AppTest(TestCase):

    def tests_check_formula(self):
        data = {
            "formula": "((A + B) * [C / D])/{W + K}"
        }
        response = self.client.post("/check_formula/", data=data, content_type="application/json")
        response_json = response.json()
        self.assertTrue(response_json["result"])
        self.assertEqual(Log.objects.filter(body=data["formula"], ipaddress="127.0.0.1", result=True).count(), 1)

        data = {
            "formula": "((A + B * [C / D])/{W + K}"
        }
        response = self.client.post("/check_formula/", data=data, content_type="application/json")
        response_json = response.json()
        self.assertFalse(response_json["result"])
        self.assertEqual(Log.objects.filter(body=data["formula"], ipaddress="127.0.0.1", result=False).count(), 1)

        data = {
            "formula": ""
        }
        response = self.client.post("/check_formula/", data=data, content_type="application/json")
        response_json = response.json()
        self.assertEqual(response_json["formula"][0], 'This field may not be blank.')
        print(Log.objects.values())
