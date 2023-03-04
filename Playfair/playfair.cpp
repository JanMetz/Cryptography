#include "playfair.hpp"

#include <string>
#include <array>
#include <vector>
#include <algorithm>
#include <utility>


Playfair::Playfair(const std::string& key) 
{
	validateKey(key);
	createMatrix();
}

void Playfair::validateKey(const std::string& key)
{
    mKey = key;
	if (mKey.size() > 25)
		throw "Invalid key provided!";

	if (mKey != "")
	{
		auto sorted = mKey;
		std::sort(sorted.begin(), sorted.end());

		for (int i = 0; i < sorted.size() - 1; ++i)
		{
			if (sorted[i] == sorted[i + 1])
				throw "Invalid key provided!";
		}
	}
    
	auto pos = mKey.find("j");
	while (pos != std::string::npos)
	{
		mKey = mKey.replace(pos, 1, "i");
		pos = mKey.find("j");
	}
}

std::string Playfair::cipher(const std::string &plainText) const
{
	auto chopped = chopMessage(plainText);

	std::string codedText("");
	for (const auto& pair : chopped)
	{
		const auto in1 = getIndexes(pair[0]);
		const auto in2 = getIndexes(pair[1]);

		codedText += getCodedLetters(in1, in2, 1);
	}
	
	return codedText;
}

std::string Playfair::decipher(const std::string &cipheredText) const
{
	auto chopped = chopMessage(cipheredText);

	std::string plainText("");
	for (const auto& pair : chopped)
	{
		const auto in1 = getIndexes(pair[0]);
		const auto in2 = getIndexes(pair[1]);

		plainText += getCodedLetters(in1, in2, -1);
	}
	
	return plainText;
}

std::string Playfair::getCodedLetters(const std::pair<int, int> &in1, const std::pair<int,int> &in2, const int addVal) const
{
	const auto row1 = in1.first;
	const auto row2 = in2.first;

	const auto col1 = in1.second;
	const auto col2 = in2.second;

	if (row1 == row2)
	{
		return std::string(1, static_cast<char>(mMatrix[row1][(col1 + addVal) % 5])) + 
		       std::string(1, static_cast<char>(mMatrix[row2][(col2 + addVal) % 5]));
	}
	else if (col1 == col2)
	{
		return std::string(1, static_cast<char>(mMatrix[(row1 + addVal) % 5][col1])) +
		       std::string(1, static_cast<char>(mMatrix[(row2 + addVal) % 5][col2]));
	}
	else
	{
		return std::string(1, static_cast<char>(mMatrix[row1][col2])) +
		       std::string(1, static_cast<char>(mMatrix[row2][col1]));
	}

	return "";
}

std::pair<int,int> Playfair::getIndexes(const char &letter) const
{
	for (const auto &row : mMatrix)
	{
		for (const auto &element : row)
			if (element == letter)
				return {std::distance(mMatrix.cbegin(), &row), std::distance(row.cbegin(), &element)};
	}

	return {-1, -1};
}

std::vector<std::array<char, 2>> Playfair::chopMessage(const std::string& msg) const
{	
	std::string curated = msg;
	std::transform(curated.begin(), curated.end(), curated.begin(), [&](unsigned char c){ return std::tolower(c); });

	auto it = curated.find(" ");
	while (it != std::string::npos)
	{
		curated = curated.replace(it, 1, "");
		it = curated.find(" ");
	}

	if (curated.size() % 2 != 0)
		curated += mReplacementChar;
	
	std::vector<std::array<char, 2>> chopped;
	for (int i = 0; i < curated.size() - 1; i += 2)
		chopped.push_back({ curated[i], curated[i + 1] });	

	return chopped;
}

void Playfair::createMatrix()
{
	std::string combined = mKey;

	for (const auto& letter : mAlphabet)
	{
		if (mKey.find(letter) == -1)
			combined += letter;
	}

	int i = 0;
	int j = 0;
	for (const auto& letter : combined)
	{
		if (i >= 5)
		{
			i = 0;
			j++;
		}

		mMatrix[j][i++] = letter;
	}
}