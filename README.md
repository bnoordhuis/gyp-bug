## the bug

    $ (cd b/ && gyp --depth=. build.gyp && make V=1)
      cc      -MMD -MF out/Default/.deps/out/Default/obj.target/a/../a/a.o.d.raw  -c -o out/Default/obj.target/a/../a/a.o ../a/a.c
      rm -f out/Default/obj.target/../a/liba.a && ar crsT out/Default/obj.target/../a/liba.a out/Default/obj.target/a/../a/a.o
      cc      -MMD -MF out/Default/.deps/out/Default/obj.target/b/b.o.d.raw  -c -o out/Default/obj.target/b/b.o b.c
      flock out/Default/linker.lock g++   -o out/Default/b -Wl,--start-group out/Default/obj.target/b/b.o out/Default/obj.target/../a/liba.a -Wl,--end-group 
    out/Default/obj.target/../a/liba.a: could not read symbols: No such file or directory
    collect2: ld returned 1 exit status
    make: *** [out/Default/b] Error 1

    $ strace -e open,stat nm b/out/Default/a/liba.a
    open("/etc/ld.so.cache", O_RDONLY)      = 3
    open("/usr/lib/libbfd-2.20.1-system.20100303.so", O_RDONLY) = 3
    open("/lib/libdl.so.2", O_RDONLY)       = 3
    open("/lib/libz.so.1", O_RDONLY)        = 3
    open("/lib/libc.so.6", O_RDONLY)        = 3
    stat("b/out/Default/a/liba.a", {st_mode=S_IFREG|0644, st_size=220, ...}) = 0
    stat("b/out/Default/a/liba.a", {st_mode=S_IFREG|0644, st_size=220, ...}) = 0
    open("b/out/Default/a/liba.a", O_RDONLY) = 3
    stat("b/out/Default/a/../../a/../a/a.o", 0x7fff68220a50) = -1 ENOENT (No such file or directory)
    open("b/out/Default/a/../../a/../a/a.o", O_RDONLY) = -1 ENOENT (No such file or directory)
    stat("b/out/Default/a/../../a/../a/a.o", 0x7fff68220af0) = -1 ENOENT (No such file or directory)
    open("b/out/Default/a/../../a/../a/a.o", O_RDONLY) = -1 ENOENT (No such file or directory)
    nm: b/out/Default/a/liba.a: No such file or directory
