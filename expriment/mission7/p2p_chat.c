#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <pthread.h>

#define PORT 40000
#define BUF_SIZE 1024

void *receive_message(void *socket_desc);

int main(int argc, char *argv[])
{
    int sock_fd;
    struct sockaddr_in peer_addr;
    pthread_t recv_thread;
    char buffer[BUF_SIZE];
    int len, size;

    if (argc != 2)
    {
        printf("Usage: %s <peer_ip>\n", argv[0]);
        return 1;
    }

    // 创建socket
    if ((sock_fd = socket(AF_INET, SOCK_DGRAM, 0)) == -1)
    {
        perror("Failed to create socket");
        return 1;
    }

    // 设置对等方信息
    memset(&peer_addr, 0, sizeof(peer_addr));
    peer_addr.sin_family = AF_INET;
    peer_addr.sin_port = htons(PORT);
    peer_addr.sin_addr.s_addr = inet_addr(argv[1]);

    // 创建接收消息的线程
    if (pthread_create(&recv_thread, NULL, receive_message, &sock_fd) != 0)
    {
        perror("Failed to create thread");
        return 1;
    }
    else
    {
        printf("Receive thread successfully started.\n");
    }

    // 循环发送消息
    while (1)
    {
        printf("Enter message: ");
        fgets(buffer, BUF_SIZE, stdin);
        len = sizeof(peer_addr);
        size = sendto(sock_fd, buffer, strlen(buffer), 0, (struct sockaddr *)&peer_addr, len);
        if (size < 0)
        {
            perror("Failed to send message");
            break;
        }
    }

    close(sock_fd);
    return 0;
}

void *receive_message(void *socket_desc)
{
    int sock = *(int *)socket_desc;
    char buffer[BUF_SIZE];
    struct sockaddr_in sender_addr;
    int sender_len = sizeof(sender_addr);
    int recv_len;

    while (1)
    {
        printf("listening for message");
        fflush(stdout);
        memset(buffer, 0, BUF_SIZE);
        recv_len = recvfrom(sock, buffer, BUF_SIZE, 0, (struct sockaddr *)&sender_addr, &sender_len);
        if (recv_len > 0)
        {
            printf("Received message: %s", buffer);
            fflush(stdout);
        }
        if (recv_len == -1)
        {
            perror("recvfrom failed");
        }
    }

    return NULL;
}
