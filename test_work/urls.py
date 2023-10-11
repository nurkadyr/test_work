from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

from app.views import CheckFormula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_formula/', CheckFormula.as_view()),
    path('docs/', schema_view),
]
