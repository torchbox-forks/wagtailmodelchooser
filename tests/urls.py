from django.urls import include, re_path
from wagtail import urls as core_urls
from wagtail.admin import urls as admin_urls

urlpatterns = [
    re_path(r"^admin/", include(admin_urls)),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    re_path(r"", include(core_urls)),
]
