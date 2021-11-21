from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.common.views import HomeView, SignUpView, DashboardView, ProfileUpdateView, ProfileView, DrawView, UploadView
from django.contrib.auth import views as auth_views
# from savedrawnimage.views2 import get_slice_by_related_image_stack_id
from savedrawnimage.views4 import SaveDrawnImageView
from saveuploadimage.views import SaveUploadImageView
from fetchimage.views import FetchImageView
from fetchprefname.views import FetchPrefNameView, SavePrefNameView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^/draw/imagestack/(?P<related_img_stack_id>\d+)', get_slice_by_related_image_stack_id),
    # path('draw/imagestack/<path:related_img_stack_id>', get_slice_by_related_image_stack_id),
    path('', HomeView.as_view(), name='home'),
    path('draw/savedrawnimage/<path:base64image>', SaveDrawnImageView),
    path('upload/saveuploadimage/<path:base64image>', SaveUploadImageView),
    path('fetchimage/', FetchImageView, name='fetchimage'),
    path('fetchprefname/', FetchPrefNameView, name='fetchprefname'),
    path('saveprefname/<str:PreferredName>', SavePrefNameView, name='saveprefname'),
    path('register/', SignUpView.as_view(), name="register"),

    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'
    ),
        name='login'
    ),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ),
        name='logout'
    ),

    path(
        'change-password',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('draw/', DrawView.as_view(), name='draw'),
    path('upload/', UploadView.as_view(), name='upload'),
    

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
