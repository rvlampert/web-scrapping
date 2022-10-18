install-dependencies:
	@echo "--> Installing Python dependencies"
	@pip install -r requirements-dev.txt

docker-build:
	@echo "--> Building Docker..."
	docker build -t web_scrapping .

docker-run:
	@echo "--> Running Docker solution..."
	docker run -it --rm --volume ${PWD}/results:/results web_scrapping

run-spider:
	@echo "--> Running spider..."
	python main.py spider

run-scrapping:
	@echo "--> Running scrapper..."
	python main.py scrapper

run:
	@echo "--> Running spider and scrapper..."
	python main.py

test:
	@echo "--> Running tests..."
	pytest . -vv
