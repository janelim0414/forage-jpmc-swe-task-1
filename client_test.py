import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, quote['top_bid']['price'])
      self.assertEqual(ask_price, quote['top_ask']['price'])
      self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
    

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, quote['top_bid']['price'])
      self.assertEqual(ask_price, quote['top_ask']['price'])
      self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getRatio_numeratorGreaterThanDenomiator(self):
    price_a = 300
    price_b = 240
    self.assertEqual(getRatio(price_a, price_b), 300/240)
  
  def test_getRatio_denominatorGreaterThanNumerator(self):
    price_a = 200
    price_b = 240
    self.assertEqual(getRatio(price_a, price_b), 200/240)
  
  def test_getRatio_zeroDenomiator(self):
    price_a = 300
    price_b = 0
    self.assertEqual(getRatio(price_a, price_b), None)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
