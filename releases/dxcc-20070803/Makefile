# dxcc Makefile -- Fabian Kurz, DJ1YFK -- http://fkurz.net/ham/dxcc.html

VERSION = `date +%Y%m%d`
DESTDIR ?= /usr

install:
	install -d -v            $(DESTDIR)/share/man/man1/
	install -m 0644 dxcc.1   $(DESTDIR)/share/man/man1/
	install -m 0755 dxcc     $(DESTDIR)/bin/
	
uninstall:
	rm -f $(DESTDIR)/bin/dxcc
	rm -f $(DESTDIR)/share/man/man1/dxcc.1

clean:
	rm -f *~

dist:
	rm -f releases/dxcc-$(VERSION).tar.gz
	rm -rf releases/dxcc-$(VERSION)
	mkdir dxcc-$(VERSION)
	cp dxcc COPYING dxcc.1 README Makefile dxcc-$(VERSION)
	tar -zcf dxcc-$(VERSION).tar.gz dxcc-$(VERSION)
	mv dxcc-$(VERSION) releases/
	mv dxcc-$(VERSION).tar.gz releases/
