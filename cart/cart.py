from django.conf import settings
from main.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        # это объект, который позволяет нам сохранять данные между запросами от одного и того же пользователя.
        # Когда пользователь добавляет товар в корзину, мы сохраняем информацию о товаре в сессии, чтобы она была доступна при следующих запросах.
        cart = self.session.get(settings.CART_SESSION_ID)
        # это попытка получить данные корзины из сессии. Если данных нет, то cart будет None.
        if not cart:
            # если данных нет, то мы создаем пустую корзину и сохраняем ее в сессии под идентификатором CART_SESSION_ID.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # это атрибут, который будет использоваться для хранения данных корзины в течение жизни объекта Cart. Он будет ссылаться на данные, которые мы сохранили в сессии.

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        # мы используем строку в качестве ключа, потому что сессия может не поддерживать использование чисел в качестве ключей.
        if product_id not in self.cart:
            # если товар еще не добавлен в корзину, то мы создаем запись для него в словаре cart, где ключом будет product_id, а значением будет словарь с количеством и ценой товара.
            # мы сохраняем цену как строку, чтобы избежать проблем с сериализацией Decimal в JSON, который используется для хранения данных в сессии.
            self.cart[product_id] = {
                "quantity": 0, "price": str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True
        # это говорит Django, что данные в сессии были изменены, и их нужно сохранить. Без этого изменения не будут сохранены, и корзина не будет работать должным образом.

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # этот метод позволяет нам итерироваться по объекту Cart, как по списку или словарю.
    def __iter__(self):
        # Когда мы используем цикл for для перебора элементов в Cart, этот метод будет вызываться.
        product_ids = self.cart.keys()
        # мы извлекаем из базы данных все продукты, которые находятся в корзине, используя их идентификаторы. то есть это sql-запрос, который получает все объекты Product, у которых id совпадает с одним из id в корзине.
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            # мы добавляем к данным о товаре в корзине ссылку на сам объект Product, чтобы мы могли использовать его атрибуты (например, name, price) при отображении корзины.
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity']for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
