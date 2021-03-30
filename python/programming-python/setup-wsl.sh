# Run XLauncn app on Windows
# disable access control
export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"
