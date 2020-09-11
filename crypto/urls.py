from django.urls import path, re_path
from crypto import views

urlpatterns = [
    path('crypto/', views.CryptoView.as_view(), name = 'crypto'),
    path('crypto/q1/', views.CryptoQ1.as_view(), name = 'cryptoq1'),
    path('crypto/q2/', views.CryptoQ2.as_view(), name = 'cryptoq2'),
]