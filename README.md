# LangChain Output Parsers

This repository demonstrates the implementation of different output parsers in LangChain for converting Large Language Model (LLM) responses into structured and usable formats.

## Project Structure

```
chainchain-parser/
├── jsonoutputparser.py
├── jsonoutputparser_with_chain.py
├── pydanticoutputparser.py
├── pydanticoutputparser_with_chain.py
├── strOutputParser.py
├── str_without_OutputParser.py
├── structureoutputparser.py
├── structureoutputparser_with_chainPipeline.py
├── README.md
├── LICENSE
└── .gitignore
```

## Features

- String Output Parser
- JSON Output Parser
- Pydantic Output Parser
- Structured Output Parser
- Parser integration with LangChain chains
- Chain pipeline examples

## Prerequisites

- Python 3.10+
- LangChain
- langchain-core
- pydantic
- python-dotenv

## Installation

Clone the repository:

```bash
git clone https://github.com/ashislife/chainchain-parser.git
```

Navigate to the project directory:

```bash
cd chainchain-parser
```

Install the required dependencies:

```bash
pip install langchain langchain-core pydantic python-dotenv
```

## Usage

Run any example individually:

```bash
python str_without_OutputParser.py
```

```bash
python strOutputParser.py
```

```bash
python jsonoutputparser.py
```

```bash
python jsonoutputparser_with_chain.py
```

```bash
python pydanticoutputparser.py
```

```bash
python pydanticoutputparser_with_chain.py
```

```bash
python structureoutputparser.py
```

```bash
python structureoutputparser_with_chainPipeline.py
```

## Files

| File | Description |
|------|-------------|
| `str_without_OutputParser.py` | LLM output without using an output parser. |
| `strOutputParser.py` | Parses LLM output as plain text using `StrOutputParser`. |
| `jsonoutputparser.py` | Parses model responses into JSON format. |
| `jsonoutputparser_with_chain.py` | JSON Output Parser integrated with a LangChain chain. |
| `pydanticoutputparser.py` | Validates and parses responses using Pydantic models. |
| `pydanticoutputparser_with_chain.py` | Pydantic Output Parser integrated with a LangChain chain. |
| `structureoutputparser.py` | Demonstrates structured output parsing. |
| `structureoutputparser_with_chainPipeline.py` | Uses Structured Output Parser within a LangChain pipeline. |

## License

This project is licensed under the MIT License.
