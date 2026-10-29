CXX ?= c++
CXXFLAGS ?= -O2 -Wall -Wextra -fPIC -std=c++17
QTFLAGS := $(shell pkg-config --cflags Qt6Core Qt6Network)
QTLIBS := $(shell pkg-config --libs Qt6Core Qt6Network)

circadian: circadian.cpp
	$(CXX) $(CXXFLAGS) $(QTFLAGS) $< -o $@ $(QTLIBS)

test: test.cpp circadian.cpp
	$(CXX) $(CXXFLAGS) $(QTFLAGS) test.cpp -o test-circadian $(QTLIBS)
	./test-circadian

clean:
	rm -f circadian test-circadian

.PHONY: test clean
