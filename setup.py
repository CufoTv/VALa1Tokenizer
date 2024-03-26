from setuptools import setup, find_packages

setup(
    name='vala1tokenizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'nltk==3.6.2',
        # Add any other dependencies here
    ],
    author='DOSaAI',
    author_email='onlineenternimet@gmail.com',
    description='VALa1Tokenizer is a custom tokenizer implementation designed to tokenize text into meaningful units, such as words, punctuation, and special tokens. It provides robust tokenization capabilities for natural language processing tasks, including text classification, sentiment analysis, and machine translation. Built on the NLTK library, VALa1Tokenizer offers flexibility and ease of integration into Python-based projects. With its intuitive interface and customizable options, VALa1Tokenizer empowers developers to efficiently preprocess text data for a wide range of applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CufoTv/vala1tokenizer',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
