#!/bin/bash

 #building the rpm's the long , -> way

 make -j16 bzImage
 make -j16 modules
 make -j16 modules_install
 make -j16 install
 make -j16 rpm-pkg


