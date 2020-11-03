#!/usr/bin/make
all: run

build: Makefile Dockerfile
	docker build -t eku_training .

run: build
	docker run  -it -v ${PWD}:/app eku_training bash
