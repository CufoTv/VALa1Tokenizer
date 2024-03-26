# VALa1Tokenizer Examples

Welcome to the VALa1Tokenizer Examples! This document provides examples demonstrating how to use the VALa1Tokenizer library in various scenarios.

## Basic Tokenization

The following example demonstrates basic tokenization using the VALa1Tokenizer library:

```python
from vala1tokenizer import VALa1Tokenizer

# Create a tokenizer instance
tokenizer = VALa1Tokenizer()

# Tokenize a sample text
text = "This is a sample sentence."
tokens = tokenizer.tokenize(text)

# Print the tokens
print(tokens)
```

Output:

```
['This', 'is', 'a', 'sample', 'sentence', '.']
```

## Customization

You can customize tokenization behavior by passing additional options to the `VALa1Tokenizer` constructor. For example:

```python
from vala1tokenizer import VALa1Tokenizer

# Create a tokenizer instance with custom options
tokenizer = VALa1Tokenizer(add_prefix_space=True)

# Tokenize a sample text
text = "This is a sample sentence."
tokens = tokenizer.tokenize(text)

# Print the tokens
print(tokens)
```

Output:

```
[' This', 'is', 'a', 'sample', 'sentence', '.']
```

Feel free to explore more examples and experiment with different tokenization options to suit your needs!
