
![tests_badge](https://github.com/ethanmsl/bldr_test/actions/workflows/test-poet.yml/badge.svg)


This is the `README.md`.  It is being pulled into the markdown files by pdoc. (or you're reading it elsewhere :shrug:)
 
[This is a link to the GitHub Pages site](https://ethanmsl.github.io/bldr_test/bldr_test.html) hosting the auto-generated documentation.


This is a [link to the PyPi package](https://pypi.org/project/bldr-test/).
Which, unfortunately, need to be generated for this test case as there seems to be a bug with the [TestPyPi](https://test.pypi.org/project/bldr-test/) package.

Current version is run via an app name: `bldrtst`
It merely prints a series of lines with random numbers (fixed seed) in them.








---------------------------- old script version ----------------------
**bold**  
*italic*  
~~strikethrough~~  

# Header

Link: [bldr-test on TestPyPi](https://test.pypi.org/project/bldr-test/)

use, install:
```zsh
pip3 list
echo
pip3 install -i https://test.pypi.org/simple/ bldr-test
echo
pip3 list
```

use, run:
```zsh
python3 -m bldr_test
```

use, uninstall:
```zsh
pip3 list
echo
pip3 uninstall bldr-test
echo
pip3 list
```

(Note: `-` vs. `_` above intended.  Also note: the `echo` commands are merely for more legible output)
