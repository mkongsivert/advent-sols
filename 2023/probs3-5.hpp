 /**
 * \file prob4.hpp
 *
 * \authors Mackenzie Kong-Sivert
 *
 * \brief Declares classes for Advent of Code problems.
 */

#ifndef BITSTRING_HPP_INCLUDED
#define BITSTRING_HPP_INCLUDED 1

#include <string>
#include <vector>

std::vector<std::string> split(std::string& line, char delim);

class legend
{
    public:
        /**
         * \brief Default constructor
         * 
         * \note Will not be used; only exists for compilation
        */
        legend();

        /**
         * \brief Parameterized constructor
         * 
         * \note
        */
        legend(long long int sour, long long int dest, long long int rang);

        /**
         * \brief Determines whether a value is in the specified range
         * 
         * \param val Value to be found
        */
        bool in_range(long long int val);

        /**
         * \brief Gives the corresponding number if a value is in the specified
         *  range
         * 
         * \param val Value for which to find the corresponding number
        */
        long long int convert(long long int val);
    private:
        long long int source_;
        long long int dest_;
        long long int range_;
};


#endif // BITSTRING_HPP_INCLUDED