ifneq (,$(wildcard ./.env))
	include .env
	export
endif

run-debug:
	fastapi dev main.py