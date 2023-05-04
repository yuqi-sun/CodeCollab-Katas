# -*- coding: utf-8 -*-
import item_behaviour as behaviour


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "Aged Brie" in item.name:
                behaviour.apply_aged_brie_logic(item)
            elif "Backstage passes" in item.name:
                behaviour.apply_backstage_passes_logic(item)
            elif "Conjured" in item.name:
                behaviour.apply_conjured_logic(item)
            elif "Sulfuras" in item.name:
                pass
            else:
                behaviour.apply_general_item_logic(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
