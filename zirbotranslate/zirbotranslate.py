#! /bin/env python3

from googletrans import Translator
from argparse import ArgumentParser


parser = ArgumentParser(
	prog='zirbotranslate.py',
	description='universal translator for languages i actually use',
	epilog='default languages are: en it de fr sr hr sl cz')

parser.add_argument('text')
parser.add_argument('-s', '--source')
parser.add_argument('-t', '--target')

args = parser.parse_args()

targets = []
if args.target != None:
	print(f"translating from {args.target}")
	targets.append(args.target)
else:
	print("translating to all languages")
	targets = [ "en", "it", "de", "fr", "sr", "hr", "sl", "cs" ]

translator = Translator()
for target in targets:
	if target == args.source:
		continue
	if args.source != None:
		print(f"from {args.source} to {target}:   ", end='')
		res = translator.translate(args.text, src=args.source, dest=target)
	else:
		res = translator.translate(args.text, dest=target)
		print(f"from {res.src} to {target}:   ", end='')
	print(f"{res.text}")
