from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.Title, "IceCream")
        self.assertEqual(item.Price, 80)
        self.assertEqual(item.Inventory, 100)

