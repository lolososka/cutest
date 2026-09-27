# NeoZygisk 2.4 (289) – Supercell build

This repository builds a pinned JingMatrix/NeoZygisk 08080ef patch to skip loading the `zygisk_vector` module for `com.supercell.brawlstars` and `com.supercell.hayday` before `DlopenMem`. It preserves Vector for Samsung HOME and other processes.

Experimental binary: do not flash without a tested recovery/rollback path. This repository does not contain credentials or the user's Android logs.
