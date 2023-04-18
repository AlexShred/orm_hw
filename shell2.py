from django.db.models import Q
from blog.models import *
from django.db.models import Subquery


ar1 = Article.set([a1, a2])
ar2 = Article.set([a1, a3])


# publ_s = Publication.objects.filter(
#     author__name__icontains='@gmail.com',
#     date_published__lt='2022-02-15'
# )
#
# f'{publ_s.query}'
#
# publ_q = Publication.objects.filter(
#     Q(author__name__icontains='@gmail.com') &
#     Q(date_published__lt='2023-04-15')
# )
#
# f'{publ_q}'
#
# publ_j = Publication.objects.filter(author__name__icontains='@gmail.com') & Publication.objects.filter(date_published__lt='2022-02-15')
#
# f'{publ_j}'
#
# auth_n = Author.objects.filter(name='Нурсултан Бердиев')
# auth_d = Author.objects.filter(date_register='2021-01-04')
# auth_l = auth_n | auth_d
#
# f'{auth_l}'
#
# auth_q = Author.objects.filter(
#     Q(name='Нурсултан Бердиев') |
#     Q(date_register='2021-01-04')
#     )
#
# f'{auth_q}'
#
# auth_s = Author.objects.filter(name='Нурсултан Бердиев') | Author.objects.filter(date_register='2021-01-04')
#
# f'{auth_s}'


# ban_ver = Publication.objects.all().exclude(author__name__startswith='Вероника')
# f'{ban_ver}'
#
# banver_q = Publication.objects.filter(
#     ~Q(author__name__startswith='Вероника')
# )
# f'{banver_q}'


# author_names = Author.objects.all().only('username')
# str(author_names)


author_sub = Publication.objects.filter(
    author__in=Subquery(
        Author.objects.filter(Q(name__icontains='Вероника') | Q(name__icontains='Чынара')).values('id')
    )
)

f'{author_sub}'

