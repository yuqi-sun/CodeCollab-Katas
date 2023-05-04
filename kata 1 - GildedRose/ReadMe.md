# Requirements breakdow

## General items
- items have a `SellIn` and a `Quality` properties
	- from `day x` to `day 0` => `SellIn = SellIn - 1` and `Quality = Quality - 1`
	- from `day 0` to `- infinity` => `Quality = Quality - 2
- `Quality` range: [0, 50]

## Special items
- `Aged Brie`
	- from `day x` to `day 0` => `Quality = Quality + 1`
	- from `day 0` to `- infinity` => `Quality = Quality + 2`
- `Sulfuras`
	- `SellIn` and `Quality` never changes
	- `Quality` is 80
- `Backstage passes`
	- from `day x` to `day 11` => `Quality = Quality + 1`
	- from `day 10` to `day 6` => `Quality = Quality + 2`
	- from `day 5` to `day 0` => `Quality = Quality + 3`
	- from `day -1` to `-infinity` => `Quality = 0`
- `Conjured`
	- from `day x` to `day 0` => `Quality = Quality - 2`
	- from `day 0` to `- infinity` => `Quality = Quality - 4`

# Tests
- [x] check a general item quality
	- [ ] decreases `-1` after each day till `sell in`
	- [ ] decreases `-2` after `sell in`
	- [ ] doesn't decrease after reaching 0
- [x] check `aged brie`
	- [ ] increases `+1` after each day till `sell in`
	- [ ] increases `+2` after `sell in`
	- [ ] doesn't increase after reaching 50
- [x] check `sulfuras`
	- [ ] doesn't change
- [x] check `backstage passes`
	- [ ] increases `+1` after each day till `day 11`
	- [ ] increases `+2` after `day 10` till `day 6`
	- [ ] increase `+3` after `day 5` till `day 0`
	- [ ] doesn't increase after reaching 50
	- [ ] remains 0 after `sell in`
- [x] check `conjured`
	- [ ] decreases `-2 after each day till `sell in`
	- [ ] decreases `-4` after `sell in`
	- [ ] doesn't decrease after reaching 0

# Implementation aka thoughts dump
~~i don't know how to python
help~~

## idea
- a map that somehow contains the behaviour for each item category??
- i also vaguely remember a similar problem solved with 'decorator' pattern (?) during scala lessons at university... like `item.apply(item specific behaviour)`
- i don't know

## what i actually did
- make a file containing all constants so that i don't have random magic numbers
	- who knows, maybe one day `aged brie` doesn't increase by 2 but by 3 after the `sell in` and looking up a file containing not even 100 lines of code (20% of which are blank lines) and search for that particular `+1` is too hard
- different functions containing the logic for each item except for `sulfuras` which don't change
	- a subfunction to decrease `sell in`
	- a subfunction to change `quality` according to the delta constants and its range constraint
- `update_quality` becomes an `if (name contains xxx) then apply this` logic