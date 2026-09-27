#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
root=Path(sys.argv[1]).resolve()
commit=subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True).strip()
assert commit.startswith("08080ef"),f"Wrong upstream commit: {commit}"
p=root/"loader/src/injector/module.cpp"
s=p.read_text()
a='#include "misc.hpp"\n#include "zygisk.hpp"'
b='#include "misc.hpp"\n#include "supercell_vector_filter.hpp"\n#include "zygisk.hpp"'
c='''    for (size_t i = 0; i < size; i++) {
        auto &m = ms[i];
        if (void *handle = DlopenMem(m.memfd, RTLD_NOW);'''
d='''    for (size_t i = 0; i < size; i++) {
        auto &m = ms[i];
        // Preserve module ID i for companions and module directory access.
        // Exclude Vector only in Supercell processes, before its ELF is loaded.
        if ((flags & APP_SPECIALIZE) &&
            neo_supercell::ShouldSkipModule(process, m.name)) {
            LOGI("NeoSupercell: skipped [%s] for [%s] before DlopenMem",
                 m.name.c_str(), process);
            continue;
        }
        if (void *handle = DlopenMem(m.memfd, RTLD_NOW);'''
assert s.count(a)==1 and s.count(c)==1,"Unexpected source structure"
s=s.replace(a,b).replace(c,d)
p.write_text(s)
(root/"loader/src/injector/supercell_vector_filter.hpp").write_bytes(
    (Path(__file__).parent/"supercell_vector_filter.hpp").read_bytes())
print("PATCH_OK",commit)
