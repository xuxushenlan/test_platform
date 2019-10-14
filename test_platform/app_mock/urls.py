from django.urls import path
from app_mock.views import view_page
from app_mock.views import view_api


urlpatterns = [

    # page
    path('', view_page.mock_list),
    path('add/<int:mid>', view_page.mock_add),

    # api
    path('get_api_data/', view_api.get_api_data),
    path('save_api_data/', view_api.save_api_data),
    path('del_api/', view_api.del_api),
    path('edit_api/', view_api.edit_api),
    path('save_api/', view_api.save_api),
    path('update_api/', view_api.update_api),
    path('see_api/', view_api.see_api),
    path('get_help/', view_api.get_help),


]
