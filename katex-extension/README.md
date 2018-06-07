## Installation

Windows:

```bash
$ python setup.py build
$ python setup.py install
```

Mac/Linux:

```bash
$ python setup.py build
$ sudo python setup.py install
```

## How to use it

Has the same functionality as MathJax

## Latex/katex - known problems
### List of commands
- `\mbox`
- `\label`
- `\nonumber`
- `{\cal (*)}`
- `\` - single backslash spacing
- `\begin{align} - \end{align}`
- `\root (*) \of (*)`

### Substitution suggestions
List of substitutions which work but are open for modification
- (*) is used to represent inputs, when multiple they are to be interpreted respectively in the New column
- "-" means it can be left empty without affecting the html endproduct

<center>

| Old        | New           |
| ------------- |:--------------|
| `\mbox`      | `\text` |
| `\label`      | -      |
| `\nonumber` | -      |
| `{\cal (*)}` | `\mathcal{(*)}`      |
| ` \ ` | ` \; `      |
| `\begin{align} - \end{align}` | `\begin{aligned} - \end{aligned}`      |
| `\root (*) \of (*)` | `\sqrt[(*)]{(*)}`      |

</center>