#pragma once
#include <cstring>
#include <string>
namespace neo_supercell {
inline bool IsTargetProcess(const char* process) {
    if (!process) return false;
    constexpr const char* packages[] = {"com.supercell.brawlstars", "com.supercell.hayday"};
    for (const char* pkg : packages) {
        size_t len = std::strlen(pkg);
        if (std::strncmp(process, pkg, len) == 0 && (process[len] == '\0' || process[len] == ':'))
            return true;
    }
    return false;
}
inline bool ShouldSkipModule(const char* process, const std::string& module_name) {
    return module_name == "zygisk_vector" && IsTargetProcess(process);
}
} // namespace neo_supercell
