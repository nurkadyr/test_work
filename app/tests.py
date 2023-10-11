from django.test import TestCase


# Create your tests here.
class AppTest(TestCase):

    def tests_check_formula(self):
        data = {
            "formula": "((A + B) * [C / D])/{W + K}"
        }
        response = self.client.post("/check_formula/", data=data, content_type="application/json")
        response_json = response.json()
        self.assertTrue(response_json["result"])

        data = {
            "formula": "((A + B * [C / D])/{W + K}"
        }
        response = self.client.post("/check_formula/", data=data, content_type="application/json")
        response_json = response.json()
        self.assertFalse(response_json["result"])

        data = {
            "formula": ""
        }
        response = self.client.post("/check_formula/", data=data, content_type="application/json")
        response_json = response.json()
        self.assertEqual(response_json["formula"][0], 'This field may not be blank.')
