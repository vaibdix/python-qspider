# threads which are running in the background -- are daemon thread
# main objective of daemon thread is to provide support for non daemon threads ie main thread eg garbage collector
# whenever main thread runs on low memory immediately PVM runs garbage collector to destroy useless obj and to provide
# free memory so that main thread can continue to execution without having any memory problem
# we can check weather thread is  daemon on not by using isdaemon() of thread class or by using thread property
#