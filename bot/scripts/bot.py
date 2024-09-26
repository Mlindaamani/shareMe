
from bot.models import Category, Author, Book
from django.db.models import Q, F, Count, Max,  StdDev, Avg, Variance, Min, Sum


def run():
    pass
    # Get all products whose prices is between 200 and 300 inclusive
    # query = Q(price__gt=400) & Q(category='Romance')
    # books = Book.objects.filter(query)
    # for book in books:
    #     print(book.name, book.price)

    # Increase the prices of the products by 10%
    # Book.objects.update(price=F('price') * 1.1)

    # price_std_dev = Book.objects.aggregate(StdDev('price'))
    # price_variance = Book.objects.aggregate(Variance('price'))
    # price_average = Book.objects.aggregate(Avg('price'))
    # min_price = Book.objects.aggregate(Min('price'))
    # max_price = Book.objects.aggregate(Max('price'))
    # sum_price = Book.objects.aggregate(Sum('price'))
    # print(f'Standard_dev: {price_std_dev}')
    # print(f'Variance: {price_variance}')
    # print(f'Average: {price_average}')
    # print(f'Min Price: {min_price}')
    # print(f'Max Price: {max_price}')
    # print(f'Sum Prices: {sum_price}')
