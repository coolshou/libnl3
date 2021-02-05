# the compiler: gcc for C program, define as g++ for C++
CC=gcc

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS=-g -Wall
LIBS=-lm

INCLUDES+=$$(pkg-config --cflags libnl-3.0 libnl-genl-3.0)
LIBS+=$$(pkg-config --libs libnl-3.0 libnl-genl-3.0)

# the build target executable:
TARGET = list_network_interfaces scan_access_points show_wifi_interface

all:  clean $(TARGET)
#@echo  Simple compiler named list_network_interfaces has been compiled

#$(TARGET): $(TARGET).c
#	$(CC) -o $@ $(TARGET).c   $(CFLAGS) $(INCLUDES)

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) $(INCLUDES) $(LIBS) -c -o $@ $<

list_network_interfaces: list_network_interfaces.o
	$(CC) -o $@ $^ $(CFLAGS) $(INCLUDES) $(LIBS)

scan_access_points: scan_access_points.o
	$(CC) -o $@ $^ $(CFLAGS) $(INCLUDES) $(LIBS)

show_wifi_interface: show_wifi_interface.o
	$(CC) -o $@ $^ $(CFLAGS) $(INCLUDES) $(LIBS)

clean:
	$(RM) $(TARGET)
