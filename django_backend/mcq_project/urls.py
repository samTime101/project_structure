from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,  TokenRefreshView,)

# ---------------_ADDED BY SAMIP REGMI---------------
from signup_app.views import SignUpView
from signin_app.views import SignInView
from user_data.views import UserDataView
from create_category.views import CreateCategoryView
from create_subcategory.views import CreateSubCategoryView
# -----------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),

    # ------------__ADDED BY SAMIP REGMI---------------

    path('api/signup/',SignUpView.as_view(), name='signup'),
    path('api/signin/', SignInView.as_view(), name='signin'),

    path('api/user/', UserDataView.as_view(),name='user_data'),

    path('api/create/category/',CreateCategoryView.as_view(),name='create_category'),
    path('api/create/subcategory/',CreateSubCategoryView.as_view(),name='create_subcategory'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ------------------------------------------------------
]
