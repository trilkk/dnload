/// \file
/// "Hello World!" example.

//######################################
// Include #############################
//######################################

#include "dnload.h"

//######################################
// Main ################################
//######################################

#if defined(DNLOAD_USE_LD)
int main()
#else
void _start()
#endif
{
    dnload();
    dnload_puts("Hello World!");

#if defined(DNLOAD_USE_LD)
    return 0;
#else
    asm_exit();
#endif
}

//######################################
// End #################################
//######################################

