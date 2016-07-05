FROM ubuntu:16.04

RUN apt update

RUN apt-get install -y  python2.7-dev cmake
RUN pip install numpy

RUN cd ~ && git clone https://github.com/Itseez/opencv.git &&\
    cd opencv && git checkout 3.0.0

RUN cd ~ &&  git clone https://github.com/Itseez/opencv_contrib.git &&\
    cd opencv_contrib && git checkout 3.0.0

RUN  cd ~/opencv && mkdir build && cd build && cmake  -D CMAKE_BUILD_TYPE=RELEASE \
            -D CMAKE_INSTALL_PREFIX=/usr/local \
            -D INSTALL_C_EXAMPLES=ON \
            -D INSTALL_PYTHON_EXAMPLES=ON \
            -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
            -D BUILD_EXAMPLES=ON ..

RUN cd ~/opencv/build && make -j8
RUN cd ~/opencv/build && make install && ldconfig
RUN apt install -y libgtk2.0-dev
#RUN pkg-config