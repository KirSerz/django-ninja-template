from logging import getLogger

from django.contrib.admin import AdminSite, site


logger = getLogger(__name__)


class CustomAdminSite(AdminSite):
    def __init__(self, *args, **kwargs):
        super(CustomAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)

        for _, model_admin in self._registry.items():
            model_admin.admin_site = self

    def get_urls(self):
        admin_urls = super().get_urls()
        custom_urls = []
        return custom_urls + admin_urls

    def get_app_list(self, request, app_label=None):
        """Return a sorted list of all the installed apps that have been registered in this site."""
        apps = []
        return super().get_app_list(request, app_label) + apps


admin_site = CustomAdminSite()
