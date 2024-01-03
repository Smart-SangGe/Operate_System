# Makefile for compiling server and client

CC = gcc
CFLAGS = -Wall
TARGETS = server client

all: $(TARGETS)

server: server.c
    $(CC) $(CFLAGS) -o $@ $^

client: client.c
    $(CC) $(CFLAGS) -o $@ $^

clean:
    rm -f $(TARGETS)
