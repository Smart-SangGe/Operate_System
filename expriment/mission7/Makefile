# Makefile for compiling server and client

CC = gcc
CFLAGS = -Wall
TARGETS = server client p2p

all: $(TARGETS)

server: server.c
	$(CC) $(CFLAGS) -o $@ $^

client: client.c
	$(CC) $(CFLAGS) -o $@ $^

p2p: p2p_chat.c
	$(CC) $(CFLAGS) -lpthread -o $@ $^

clean:
	rm -f $(TARGETS)
