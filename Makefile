# Makefile for source rpm: krb5
# $Id$
NAME := krb5
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
