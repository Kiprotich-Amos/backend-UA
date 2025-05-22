from django.urls import path
from .viewpoint.auth import LoginAPIView, RegisterAPIView, RoleAPIView
from .viewpoint.warehouse_views import GeneralCargoListCreateAPIView, GeneralCargoDetailAPIView,CargoItemReleaseListCreateAPIView, CargoItemReleaseDetailAPIView, OperationTableListCreateAPIView, OperationTableDetailAPIView, ContractListCreateAPIView, ContractDetailAPIView
# from .viewpoint.role_views import  RoleAPIView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('roles/', RoleAPIView.as_view(), name='roles'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     # General Cargo URLs
    path('general-cargo/', GeneralCargoListCreateAPIView.as_view(), name='general-cargo-list-create'),
    path('general-cargo/<int:pk>/', GeneralCargoDetailAPIView.as_view(), name='general-cargo-detail'),

    # Cargo Item Release URLs
    path('cargo-item-release/', CargoItemReleaseListCreateAPIView.as_view(), name='cargo-item-release-list-create'),
    path('cargo-item-release/<int:pk>/', CargoItemReleaseDetailAPIView.as_view(), name='cargo-item-release-detail'),

    # Operation Table URLs
    path('operation-table/', OperationTableListCreateAPIView.as_view(), name='operation-table-list-create'),
    path('operation-table/<int:pk>/', OperationTableDetailAPIView.as_view(), name='operation-table-detail'),

    # Contract URLs
    path('contracts/', ContractListCreateAPIView.as_view(), name='contract-list-create'),
    path('contracts/<int:pk>/', ContractDetailAPIView.as_view(), name='contract-detail'),

]