#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
import hashlib
out=Path("neo/module/build/outputs/release")
archives=sorted(out.glob("NeoZygisk-*-debug.zip"))
assert len(archives)==1, f"Expected one debug ZIP: {archives}"
p=archives[0]
with ZipFile(p) as z:
 assert z.testzip() is None
 names=set(z.namelist())
 assert "module.prop" in names
 prop=z.read("module.prop").decode()
 assert "id=zygisksu" in prop and "versionCode=289" in prop,prop
 libs=[n for n in names if n.endswith("/libzygisk.so") and "/arm64-v8a/" in n]
 assert len(libs)==1, libs
 data=z.read(libs[0])
 assert data.startswith(b"\x7fELF")
 assert b"NeoSupercell: skipped" in data,"Patch marker missing from ARM64 native binary"
 verified=0
 for name in names:
  if name.endswith(".sha256"):
   base=name[:-7]
   assert base in names,base
   expected=z.read(name).decode().strip().split()[0]
   assert hashlib.sha256(z.read(base)).hexdigest()==expected,base
   verified+=1
 assert verified>=12,verified
print("BUILD_ZIP_OK",p)
print("SHA256",hashlib.sha256(p.read_bytes()).hexdigest())
print("VERIFIED_SIDECARS",verified)
