from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Log
from app.serializers import FormulaSerializer
from app.utils import get_client_ip


class CheckFormula(APIView):

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = {"request": self.request}
        return FormulaSerializer(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        result = False

        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        if serializer.is_valid(raise_exception=True):
            clean_formula = ""
            formula = serializer.data.get("formula")
            for char in formula:
                if char not in {"(", ")", "[", "]", "{", "}"}:
                    continue

                if clean_formula != "" and clean_formula[-1] == brackets.get(char):
                    clean_formula = clean_formula[:-1]
                    continue

                clean_formula += char

            result = len(clean_formula) == 0

            Log.objects.create(
                body=formula,
                ipaddress=get_client_ip(request),
                result=result
            )

        return Response({"result": result})
