> [!WARNING]
> `xorr` Only a few things work as expected in the current version. Many features haven't been implemented yet.

# Xorr

Xorr is a CLI tool to perform XOR operations!

## Features

- Generate ciphertext

## Usage

```
python xor.py 
Gimme some input: [INPUT]
Gimme a key: [KEY]
```

## Example

```
python xor.py 
Gimme some input: 10
Gimme a key: 101
```

Output:

```
The ciphertext is: 111
Decimal value: 7
```

As you can see the ciphertext gets correctly made but that isn't the case for every operation. 

Something else to note is that this same operation gives `45` as an output on CyberChef so I will have to investigate why that's happening, my understanding of XOR must be messed up somewhere.

*See the following section for additions that have yet to be put into the program.*

## Roadmap / to-do list

- [x] Ensure list is of the same length pre-operation.
- [ ] Add ASCII support. (*50% done*)
- [ ] Add file encryption support.

## End notes

This project was started to improve my programming skills and deepen my understanding of XOR and cryptography in general.

## Information

Author: [pindjouf](https://github.com/pindjouf)

License: [MIT License](https://opensource.org/license/MIT)
