#define _GNU_SOURCE
#include <sys/socket.h>
#include <dlfcn.h>
#include <errno.h>
#include <stdlib.h>
#include <netinet/in.h>

int
connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
{
	unsigned short port;
	static int (*next_connect)(int, const struct sockaddr *, socklen_t);

	if (next_connect == NULL) {
		next_connect = dlsym(RTLD_NEXT, "connect");
		if (next_connect == NULL) {
			errno = ENOSYS;
			return -1;
		}
	}

	if (getenv("NOPORT53") == NULL) {
		return next_connect(sockfd, addr, addrlen);
	}

	switch (addr->sa_family) {
	case AF_INET:
		port = ntohs(((struct sockaddr_in *)addr)->sin_port);
		if (port == 53) {
			errno = ECONNREFUSED;
			return -1;
		}
		break;
	case AF_INET6:
		port = ntohs(((struct sockaddr_in6 *)addr)->sin6_port);
		if (port == 53) {
			errno = ECONNREFUSED;
			return -1;
		}
		break;
	default:
		break;
	}
	return next_connect(sockfd, addr, addrlen);
}

ssize_t
sendto(int sockfd, const void *buf, size_t len, int flags,
       const struct sockaddr *dest_addr, socklen_t addrlen)
{
	unsigned short port;
	static int (*next_sendto)(int, const void *, size_t, int,
				  const struct sockaddr *, socklen_t);

	if (next_sendto == NULL) {
		next_sendto = dlsym(RTLD_NEXT, "sendto");
		if (next_sendto == NULL) {
			errno = ENOSYS;
			return -1;
		}
	}

	if (getenv("NOPORT53") == NULL) {
		return next_sendto(sockfd, buf, len, flags, dest_addr, addrlen);
	}

	switch (dest_addr->sa_family) {
	case AF_INET:
		port = ntohs(((struct sockaddr_in *)dest_addr)->sin_port);
		if (port == 53) {
			errno = ECONNREFUSED;
			return -1;
		}
		break;
	case AF_INET6:
		port = ntohs(((struct sockaddr_in6 *)dest_addr)->sin6_port);
		if (port == 53) {
			errno = ECONNREFUSED;
			return -1;
		}
		break;
	default:
		break;
	}
	return next_sendto(sockfd, buf, len, flags, dest_addr, addrlen);
}
