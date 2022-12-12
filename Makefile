# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
.ONESHELL:

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

create-module: ## example: make create-module module=is_before
	cd ./pydate \
	&& mkdir $(module) \
	&& cd $(module) \
	&& touch __init__.py \
	&& touch $(module).py \
	&& touch test.py \
	&& echo "from .$(module) import $(module)" > __init__.py \
	&& echo "def $(module)(): pass" > $(module).py \ 
	&& echo "class Test: pass" > test.py

test-install: 
	python -c "import pydate"