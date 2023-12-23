/**
 * \file probs3-5.cpp
 *
 * \authors Mackenzie Kong-Sivert
 *
 * \brief Implements the Advent of Code solutions.
 */

#include "probs3-5.hpp"

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

#define MIN(a, b) ((a < b) ? a : b)
#define MAX(a, b) ((a > b) ? a : b)

std::vector<std::string> split(std::string& line, char delim=' ')
{
    std::vector<std::string> word_list;
    std::string curr;
    for (auto itr = line.begin(); itr!=line.end(); ++itr)
    {
        if (*itr==delim)
        {
            if (curr!="")
            {
                word_list.push_back(curr);
                curr = "";
            }
        }
        else
        {
            curr.push_back(*itr);
        }
    }
    word_list.push_back(curr);
    return word_list;
}

legend::legend() :
        source_{0}, dest_{0}, range_{0}
{
    // Nothing to do here
}

legend::legend(long long int sour, long long int dest, long long int rang) :
        source_{sour}, dest_{dest}, range_{rang}
{
    // Nothing to do here
}

bool legend::in_range(long long int val)
{
    return (val >= source_) and (val <= source_+range_);
}

long long int legend::convert(long long int val)
{
    if (dest_ >= source_)
    {
        return val + (dest_ - source_);
    }
    else
    {
        return val - (source_ - dest_);
    }
}

std::vector<legend> load_map(std::ifstream & file)
{
    std::string str;
    std::vector<legend> legend_list;
    std::getline(file, str); // Throw away label line
    while (std::getline(file, str))
    {
        if (str == "")
        {
            break;
        }
        std::vector<std::string> temp = split(str);
        legend_list.push_back(legend(stoll(temp[1]), stoll(temp[0]), stoll(temp[2])));
    }
    return legend_list;
}

int prob3()
{
    // Height and width of document
    size_t h = 140;
    size_t w = 141;
    std::ifstream file("gondolas.txt");
    // Read file text into 2d char array schem
    char schem[h][w];
    std::string str;
    size_t i = 0;
    while (std::getline(file, str))
    {
        size_t j = 0;
        for (auto itr = str.begin(); itr != str.end(); ++itr)
        {
            schem[i][j] = *itr;
            ++j;
        }
        ++i;
    }
    uint sumparts = 0;
    for (size_t i = 0; i < h; ++i)
    {
        for (size_t j = 0; j < w; ++j)
        {
            size_t a = (j==0) ? 0 : j-1;
            size_t b = j;
            if (isdigit(schem[i][j]))
            {
                while (isdigit(schem[i][j]))
                {
                    ++j;
                    if (j == w-1)
                    {
                        break;
                    }
                }
                std::cout << std::string(schem[i]).substr(b, j-b) << std::endl;
                uint to_add = std::stoi(std::string(schem[i]).substr(b, j-b));
                // check i-1 a to j
                // check i a and j
                // check i+1 a to j
                if (ispunct(schem[i][a]) and schem[i][a]!='.')
                {
                    std::cout << "Added" << std::endl;
                    sumparts += to_add;
                }
                else if (ispunct(schem[i][j]) and schem[i][j]!='.')
                {
                    std::cout << "Added" << std::endl;
                    sumparts += to_add;
                }
                else {
                    bool part = false;
                    for (size_t k = a; k <= j; ++k)
                    {
                        if (i > 0 and ispunct(schem[i-1][k]) and schem[i-1][k]!='.')
                        {
                            part = true;
                            break;
                        }
                        else if (i<h-1 and ispunct(schem[i+1][k]) and schem[i+1][k]!='.')
                        {
                            part = true;
                            break;
                        }
                    }
                    if (part)
                    {
                        std::cout << "Added" << std::endl;
                        sumparts += to_add;
                    }
                    else
                    {
                        std::cout << "i = " << i << "; j = " << j << std::endl;
                    }
                }
                --j;
            }
        }
    }
    std::cout << "The sum is " << sumparts << std::endl;
    

    
    return 0;
}

int prob4()
{
    std::ifstream file("cards.txt");
    std::string str;
    size_t all_scores = 0;
    while (std::getline(file, str))
    {
        str.erase(0, str.find(':')+1);
        std::vector<std::string> two_lists = split(str, '|');
        std::vector<std::string> lucky = split(two_lists[0]);
        std::vector<std::string> hand = split(two_lists[1]);
        size_t matches = 0;
        for (auto itr1 = hand.begin(); itr1 != hand.end(); ++itr1)
        {
            for (auto itr2 = lucky.begin(); itr2 != lucky.end(); ++itr2)
            {
                if (*itr1==*itr2)
                {
                    ++matches;
                }
            }
        }
        std::cout << matches << " matches" << std::endl;
        all_scores += (matches == 0) ? 0 : pow(2, matches-1);
    }
    std::cout << "Score total: " << all_scores << std::endl;
    return 0;
}

int prob5()
{
    std::ifstream file("seed-to-soil.txt");
    // Read in seeds
    std::string str;
    std::vector<long long int> seeds;
    std::getline(file, str);
    str.erase(0, str.find(':')+1);
    std::vector<std::string> temp = split(str);
    for (auto itr = temp.begin(); itr != temp.end(); ++itr)
    {
        seeds.push_back(stoll(*itr));
    }
    std::getline(file, str); // Throw away blank line
    // Read in seeds to soil
    std::vector<legend> stos = load_map(file);
    // Read in soil to fertilize
    std::vector<legend> stof = load_map(file);
    // Read in fertilizer to water
    std::vector<legend> ftow = load_map(file);
    // Read in water to light
    std::vector<legend> wtol = load_map(file);
    // Read in light to temperature
    std::vector<legend> ltot = load_map(file);
    // Read in temperature to humidity
    std::vector<legend> ttoh = load_map(file);
    // Read in humidity to location
    std::vector<legend> htol = load_map(file);
    std::vector<legend> pipeline[7] = {stos, stof, ftow, wtol, ltot, ttoh, htol};
    
    // Conversions
    std::vector<long long int> curr = seeds;
    for (uint8_t i = 0; i<7; ++i)
    {
        std::vector<long long int> next;
        for (auto sitr = curr.begin(); sitr != curr.end(); ++sitr)
        {
            for (auto mitr = pipeline[i].begin(); mitr != pipeline[i].end(); ++mitr)
            {
                if (mitr->in_range(*sitr)) // corresponding rule found
                {
                    //std::cout << int(i) << ": " << *sitr << " goes to " << mitr->convert(*sitr) << std::endl;
                    next.push_back(mitr->convert(*sitr));
                    goto match_found; //abort inner loop & continue outer loop
                }
            }
            // Corresponding rule not found, default to same number
            //std::cout << int(i) << ": No match for " << *sitr << std::endl;
            next.push_back(*sitr); 
            match_found:;
        }
        curr = next;
    }

    // Find the smallest result
    long long int sm_res = INT64_MAX;
    for (auto ritr = curr.begin(); ritr != curr.end(); ++ritr)
    {
        sm_res = MIN(sm_res, *ritr);
    }
    std::cout << "The smallest required humidity value is " << sm_res << std::endl;
    return 0;
}

int main()
{
    return prob5();
}