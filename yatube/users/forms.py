from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


# Форма для создания пользователя
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # указываем модель для взаимодействия
        model = User
        # указываем поля которые видны в форме и будут доступны в порядке
        fields = ['first_name', 'last_name', 'username', 'email']
