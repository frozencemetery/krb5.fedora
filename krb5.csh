if ( /usr/kerberos/bin !~ "${path}" ) then
	set path = ( /usr/kerberos/bin $path )
endif
if ( /usr/kerberos/sbin !~ "${path}" ) then
	if ( `id -u` == 0 ) then
		set path = ( /usr/kerberos/sbin $path )
	endif
endif
