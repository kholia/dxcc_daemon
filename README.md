#### Setup (for Debian / Ubuntu)

```
sudo apt install perl libjson-perl
```

Note: This code will need to be modified before it is usable for you.


#### Usage

Launch the `dxcc_daemon`.

```
./dxcc_daemon.pl
```

Query the `DXCC Daemon` using the following command:

```
$ output=$(echo 'HC1MD/2' | netcat -q 1 localhost 7373)

$ print "$output"
{"callsign":"HC1MD/2","distance":16516,"country":"Ecuador"}
```

OR

```
$ ./client.py
```


#### Why?

The `dxcc` program by `Fabian Kurz` is very reliable (compared to `pyhamtools`)
for doing callsign lookups.

To make realtime fast lookups possible (by hooking into WSJT-X), we decided
to write this small daemon wrapper around the `dxcc` program.


#### Notes

Please excuse my Perl - I don't know any ;)

In its current form, this is suitable for local single-threaded usage only.

Upstream is at https://fkurz.net/ham/dxcc.html.

Download updated 'cty.dat' ("Big CTY") files from http://www.country-files.com/ site.
