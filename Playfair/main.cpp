#include "playfair.hpp"

#include <iostream>


int main()
{
    try
    {
        Playfair pf("aghjul");

        std::cout << pf.cipher("text to cipher") << std::endl;
        std::cout << pf.decipher("zozrztdhract") << std::endl;
    }
    catch(const char *msg)
    {
        std::cout << msg << std::endl;
    }

    return 0;
}