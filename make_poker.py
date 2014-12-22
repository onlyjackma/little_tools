#!/usr/bin/env python
from pprint import pprint
from random import shuffle

values = range(1,11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
decks = ['%s of %s' % (v,s) for v in values for s in suits]

pprint(decks[:12])
shuffle(decks)
pprint(decks[:12])

