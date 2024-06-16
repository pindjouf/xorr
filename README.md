# Xorr

Xorr is a CLI utility to perform XOR operations on binary values (for now).

P.S. Nothing works yet.

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

Something else to note is that this same operation gives `45` as an output on CyberChef so I will have to investigate as to why that's happening my understanding of XOR must be messed up somewhere.

*See the following section for additions that have yet to be put into the program.*

## Roadmap / to-do list

- [ ] Ensure list is of the same length pre-operation.
- [ ] Make `xor.py` command usable in one line.
- [ ] Add ASCII support.
- [ ] Add file encryption support.

## End notes

This project was started to improve my programming skills and deepen my understanding of XOR and cryptography in general.
