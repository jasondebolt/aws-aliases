BASH_CONFIG = ~/.bash_profile

.PHONY: clean
clean:
	python aws-aliases.py clean

.PHONY: build
build:
	python aws-aliases.py

.PHONY: install
install: build
	echo "\n## AWS Service Aliases" >> $(BASH_CONFIG)
	echo "source ~/.aws_service_aliases" >> $(BASH_CONFIG)
	@echo "\n Restart your terminal session or run 'source $(BASH_CONFIG)'\n"
	@echo "\n After restarting, type 'ec2' or 's3 && route53' in your terminal\n"