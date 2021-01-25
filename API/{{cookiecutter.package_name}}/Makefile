REPO_DIR:= $(shell git rev-parse --show-toplevel)

VERSION_LINE = $(shell grep 'APP_VERSION' ${REPO_DIR}/{{cookiecutter.package_name}}/{{cookiecutter.package_name}}.cfg)

VERSION = $(shell echo ${VERSION_LINE} | sed 's/.*=//')

APP_NAME = "{{cookiecutter.package_name}}"

IMAGE_NAME = "${APP_NAME}"


.PHONY: build-image
build-image:
	@echo "+ $@"
	@docker build -t ${IMAGE_NAME}:${VERSION} .

.PHONY: run
run: build-image
	@echo "+ $@"
	@docker run -t -d ${IMAGE_NAME}:${VERSION}

.PHONY: stop
stop: $(eval SHELL:=/bin/bash)
	@echo "+ $@"
	bash -c "docker ps | grep ${IMAGE_NAME}:${VERSION} | awk '{print $1}' | xargs docker stop";

.PHONY: clean
clean:
	@echo "+ $@"
	@echo "Running python black..."
	@bash -c "black ${IMAGE_NAME}/";
	@echo "Generating pylint report..."
	@bash -c "pylint ${IMAGE_NAME}/";

.PHONY: test
test: build-image
	@echo "+ $@"
	@docker run -t --rm ${IMAGE_NAME}:${VERSION} pytest -v

.PHONY: pyshell
pyshell: build-image
	@echo "+ $@"
	@docker run -it --rm ${IMAGE_NAME}:${VERSION}
