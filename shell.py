from blog.models import *


a1 = Author.objects.create(name='Нурсултан Бердиев', email='nursultanberdiev@gmail.com', username='nursultanberdiev', date_register='2021-01-04')
a2 = Author.objects.create(name='Лю Вероника', email='ronilyu@gmail.com', username='ronik', date_register='2023-03-12')
a3 = Author.objects.create(name='Токтосунова Чынара', email='chynara0409@gmail.com', username='chynara', date_register='2023-01-21')


ar1 = Article.objects.create(title='Что нужно для разработки мобильных приложений: языки и тренды')
ar2 = Article.objects.create(title='Зачем нужно использовать кроссплатформенную систему')
ar3 = Article.objects.create(title='Сравниваем Java и Python или с чего лучше начать')
ar4 = Article.objects.create(title='Новый ChatGPT-4: в чем его особенность')
ar5 = Article.objects.create(title='История компании Boston Dynamics. Как появлялись их роботы')


p1 = Publication.objects.create(author=a1, article=ar1, date_published='2022-01-01')
p2 = Publication.objects.create(author=a1, article=ar2, date_published='2022-02-02')
p3 = Publication.objects.create(author=a1, article=ar3, date_published='2022-03-03')
p4 = Publication.objects.create(author=a2, article=ar4, date_published='2023-03-13')
p5 = Publication.objects.create(author=a3, article=ar5, date_published='2023-11-22')


python manage.py shell < shell.py
authors = Author.objects.all()
authors = authors.order_by('date_register')
authors
nurs = Article.objects.filter(name__exact='Нурсултан')
nurs
oldfag = Author.objects.filter(date_register__lt='2022-10-10')
oldfag
pub_dict = Publication.values('author', 'article')
pub_dict
pub_list = Publication.values_list('author', 'article')
pub_list
pub_b = Publication.objects.filter(name__contains='В')
pub_b