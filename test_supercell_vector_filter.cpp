#include "supercell_vector_filter.hpp"
#include <cassert>
#include <iostream>
struct Test {const char *process; const char *module; bool skip;};
int main(){
 const Test cases[]={
 {"com.supercell.brawlstars","zygisk_vector",true},
 {"com.supercell.brawlstars:remote","zygisk_vector",true},
 {"com.supercell.hayday","zygisk_vector",true},
 {"com.supercell.hayday:remote","zygisk_vector",true},
 {"com.supercell.brawlstars.fake","zygisk_vector",false},
 {"com.supercell.hayday1","zygisk_vector",false},
 {"other.com.supercell.hayday","zygisk_vector",false},
 {"com.sec.android.app.launcher","zygisk_vector",false},
 {"system_server","zygisk_vector",false},
 {"com.supercell.brawlstars","zygisk_assistant",false},
 {"com.supercell.hayday","other_module",false},
 {"com.supercell.brawlstars","zygisk_vector_fake",false},
 {"com.supercell.brawlstars","",false},
 {"","zygisk_vector",false},
 {nullptr,"zygisk_vector",false}
 };
 for(const auto &c:cases) assert(neo_supercell::ShouldSkipModule(c.process,c.module)==c.skip);
 std::cout<<"PASS "<<sizeof(cases)/sizeof(cases[0])<<" process/module tests\n";
}
