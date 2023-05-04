# -*- coding: utf-8 -*-
import unittest

from gilded_rose_refactored import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_item(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=2, quality=5)]
        gilded_rose = GildedRose(items)

        # decreases `-1` after each day till `sell in`
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

        # decreases `-2` after `sell in`
        gilded_rose.update_quality()  # sell_in 0 quality 3
        gilded_rose.update_quality()  # sell_in -1 quality 1
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

        # doesn't decrease after reaching 0
        gilded_rose.update_quality()  # sell_in -2
        gilded_rose.update_quality()  # sell_in -3
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=45)]
        gilded_rose = GildedRose(items)

        # increases `+1` after each day till `sell in`
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(46, items[0].quality)

        # increases `+2` after `sell in`
        gilded_rose.update_quality()  # sell_in 0 quality 47
        gilded_rose.update_quality()  # sell_in -1 quality 49
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(49, items[0].quality)

        # doesn't increase after reaching 50
        gilded_rose.update_quality()  # sell_in -2 quality 50
        gilded_rose.update_quality()  # sell_in -3 quality 50
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),]
        gilded_rose = GildedRose(items)

        # doesn't change
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[1].name)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(80, items[1].quality)

    def test_backstage_passes(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=30),]
        gilded_rose = GildedRose(items)

        # increases `+1` after each day till `day 11`
        gilded_rose.update_quality() # day 11 q31
        gilded_rose.update_quality() # day 10 q32
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(32, items[0].quality)

        # increases `+2` after `day 10` till `day 6`
        gilded_rose.update_quality() #day 9 q34
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(34, items[0].quality)
        gilded_rose.update_quality() #day 8 q36
        gilded_rose.update_quality() #day 7 q38
        gilded_rose.update_quality() #day 6 q40
        gilded_rose.update_quality() #day 5 q42
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(42, items[0].quality)

        # increase `+3` after `day 5` till `day 0`
        gilded_rose.update_quality() #day 4 q45
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(45, items[0].quality)
        gilded_rose.update_quality() #day 3 q48
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(48, items[0].quality)


        # doesn't increase after reaching 50
        gilded_rose.update_quality() #day 2 q48
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality() #day 1
        gilded_rose.update_quality() #day 0
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

        # remains 0 after `sell in`
        gilded_rose.update_quality() #day -1
        gilded_rose.update_quality() #day -2
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured(self):
        items = [Item(name="Conjured Mana Cake", sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)

        # decreases `-2` after each day till `sell in`
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

        # decreases `-4` after `sell in`
        gilded_rose.update_quality()  # sell_in 0 quality 6
        gilded_rose.update_quality()  # sell_in -1 quality 2
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

        # doesn't decrease after reaching 0
        gilded_rose.update_quality()  # sell_in -2
        gilded_rose.update_quality()  # sell_in -3
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
