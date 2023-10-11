from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from app.serializers import FormulaSerializer


@api_view(["POST"])
def check_formula(request: Request):
    serializer = FormulaSerializer(data=request.data)
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

    return Response({"result": result})
