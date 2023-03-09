# Laboratory Exercise 02 Part 1

Van Paul Angelo C. Dayag
2020-10106
CMSC 180 T6L

# Installation

Programming language: **Python**  
Dependencies: **pyenv, Python nogil 3.9.10**  
Main program file: **main.py**  

**Ubuntu**
Install dependencies
`apt-get update && apt-get install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils \
tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev curl git gcc python3 make`

Install pyenv
`curl https://pyenv.run | bash`


`export PYENV_ROOT="$HOME/.pyenv"`
`command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"`
`eval "$(pyenv init -)"`

Install nogil
`pyenv install nogil`

Set Python version to nogil
`pyenv local nogil`

Activate nogil
`eval "$(pyenv init -)"`

# Run

`python3 main.py [n] [t]`