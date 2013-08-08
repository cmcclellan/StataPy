# StataPy

Goal: `StataPy` aims to make it easy for Python programmers to
estimate econometric models using `Stata`.

Motivation: `Stata` is a wonderful library of econometric models, but
`Stata`'s programming language is idiosyncratic.

Approach: I hope to accomplish the above goal with the least amount of
code necessary.

## TODOS

The `format` parameter in the stata.Model constructor is a hack. I'm
not sure how to prevent rounding and also have decimal numbers between
zero and one have a leading zero.

It would be nice to handle temporary files more gracefully.

It would be nice to package this for an easy pip install from github.
