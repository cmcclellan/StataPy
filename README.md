# StataPy

Goal: `StataPy` aims to make it easy for Python programmers to
estimate econometric models using `Stata`.

Motivation: `Stata` is a wonderful library of econometric models, but
`Stata`'s programming language is less wonderful.

Approach: I hope to accomplish the above goal with the least amount of
code necessary.

## Installation

`StataPy` can be installed using pip:

    pip install -e git+https://github.com/amarder/StataPy.git#egg=StataPy

Here is a simple example of how to estimate a Stata model:

    import pandas
    import stata

    data = pandas.DataFrame({'y': [1, 2, 3, 4], 'x': [0, 1, 0, 1]})
    model = stata.Model(data, 'regress y x, robust')
    print model.estimate()

By default, stata.Model assumes that Stata can be called on your
computer with the command `stata`. If the path on your computer is
different, the correct path can be passed into the Model constructor
through the parameter `path_to_stata_binary`.

Note the example uses a `pandas.DataFrame`. This is most likely how I
will use `StataPy` but it is not a requirement. One could use a
`stata.Model` with any data object that has a `to_csv` method like a
pandas DataFrame.

## TODOS

The `format` parameter in the stata.Model constructor is a hack. I'm
not sure how to prevent rounding and also have decimal numbers between
zero and one have a leading zero.

It would be nice to handle temporary files more gracefully.

It would be nice to package this for an easy pip install from github.
