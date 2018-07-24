cmake_minimum_required (VERSION 2.8.11)
project (cpprep)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Qt5 COMPONENTS Core Widgets REQUIRED)

#include( ${QT_USE_FILE} )
#add_definitions( ${QT_DEFINITIONS} )
#include_directories( ${CMAKE_BINARY_DIR} )

find_package(ZeroMQ CONFIG REQUIRED)
include_directories( ${ZeroMQ_INCLUDE_DIRS} )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable (cpprep cpprep.cpp)


target_link_libraries (cpprep zmq ${OpenCV_LIBS} ${QT_LIBRARIES} )
