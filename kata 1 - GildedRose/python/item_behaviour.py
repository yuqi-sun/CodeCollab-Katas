import quality_delta_constant as constant


# changes the item quality according to the given delta and the range constraint
def change_quality(item, delta):
    tmp = item.quality + delta
    if tmp > constant.MAX_QUALITY:
        item.quality = constant.MAX_QUALITY
    elif tmp < constant.MIN_QUALITY:
        item.quality = constant.MIN_QUALITY
    else:
        item.quality = tmp


# decrease the sell in date
def decrease_sell_in(item):
    item.sell_in = item.sell_in - 1


# applies the logic common to item of no particular category
def apply_general_item_logic(item):
    decrease_sell_in(item)
    if item.sell_in >= 0:
        change_quality(item, constant.GENERAL_ITEM_DELTA)
    else:
        change_quality(item, constant.GENERAL_ITEM_DELTA_AFTER_SELL_IN)


# applies logic to aged brie item
def apply_aged_brie_logic(item):
    decrease_sell_in(item)
    if item.sell_in >= 0:
        change_quality(item, constant.AGED_BRIE_DELTA)
    else:
        change_quality(item, constant.AGED_BRIE_DELTA_AFTER_SELL_IN)


# applies logic to backstage passes item
def apply_backstage_passes_logic(item):
    decrease_sell_in(item)
    if item.sell_in >= 10:
        change_quality(item, constant.BACKSTAGE_PASSES_DELTA_BEFORE_DAY_10)
    elif item.sell_in >= 5:
        change_quality(item, constant.BACKSTAGE_PASSES_DELTA_BEFORE_DAY_5)
    elif item.sell_in >= 0:
        change_quality(item, constant.BACKSTAGE_PASSES_DELTA_BEFORE_DAY_0)
    elif item.sell_in < 0:
        item.quality = 0


# applies logic to the conjured item
def apply_conjured_logic(item):
    decrease_sell_in(item)
    if item.sell_in >= 0:
        change_quality(item, constant.CONJURED_DELTA)
    else:
        change_quality(item, constant.CONJURED_DELTA_AFTER_SELL_IN)

