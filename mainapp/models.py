from django.db import models


class CompanyList(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    email = models.EmailField(verbose_name='E-mail')
    logo = models.ImageField(verbose_name='Лого', upload_to='static_img', blank=True, default='')
    map = models.CharField(verbose_name='Карта', max_length=1000, default='', blank=True, help_text='Установить значение width="100%"')
    working_hours = models.TextField(verbose_name='Время работы', default='с понедельника по пятницу\nс 10.00 до 18.00')
    is_active = models.BooleanField(verbose_name='Активная фирма', default=False)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title

    def get_phone_numbers(self):
        return PhoneNumList.objects.filter(company=self.pk)


class PhoneNumList(models.Model):
    phone_num = models.CharField(max_length=20, verbose_name='Телефон')
    company = models.ForeignKey(CompanyList, verbose_name='Компания', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.phone_num


class ArticleList(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text_art = models.TextField(verbose_name='Текст')
    is_active = models.BooleanField(verbose_name='Активно', default=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title}, {self.is_active}'


class FeedbackList(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(max_length=256, verbose_name='E-mail')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.email

