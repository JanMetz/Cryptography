#ifndef PLAYFAIR_HPP
#define PLAYFAIR_HPP

#include <string>
#include <array>
#include <vector>
#include <utility>

class Playfair
{
public:
	Playfair(const std::string& key);

	std::string cipher(const std::string& plainText) const;
	std::string decipher(const std::string &cipheredText) const;

private:
	void createMatrix();
	void validateKey(const std::string& key); 
	std::vector<std::array<char, 2>> chopMessage(const std::string& msg) const;
	std::string getCodedLetters(const std::pair<int, int> &in1, const std::pair<int,int> &in2, const int addVal) const;
	std::pair<int,int> getIndexes(const char &letter) const;
	static bool checkForIllegalChars(const std::string &text);

	std::string mKey;
	const std::array<char, 25> mAlphabet{ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
	std::array<std::array<char, 5>, 5> mMatrix;

	const char mReplacementChar = 'x';
};

#endif
