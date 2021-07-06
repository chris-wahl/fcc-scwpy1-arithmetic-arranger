def arithmetic_arranger(problems, solve=False):
    decomposed = [ problem.split() for problem in problems ]

    # Error checking.
    if len(decomposed) > 5:
        return "Error: Too many problems."
    elif not all(d[1] in ('+', '-') for d in decomposed):
        return "Error: Operator must be '+' or '-'."
    elif not all(d[0].isnumeric() and d[2].isnumeric() for d in decomposed):
        return "Error: Numbers must only contain digits."
    elif not all(len(d[0]) < 5 and len(d[2]) < 5 for d in decomposed):
        return "Error: Numbers cannot be more than four digits."

    # Format the problems into properly formatted tuples.
    formatted_problems = []
    for top, operator, bottom in decomposed:
        largest = max([len(v) for v in (top, bottom, operator)])
        final = None  # Allow checking if "final" is None or not
        # If the "solve" flag is True, also solve the problem.
        if solve:
            if operator == '+':
                final = int(top) + int(bottom)
            elif operator == '-':
                final = int(top) - int(bottom)
            # Recalculate "largest" against |final|.  Do not want the "-"
            # in a negative "final" to over-pad the problem.
            largest = max(largest, len(str(abs(final))))

        # Build the first, second and third lines of this problem
        t = (
            top.rjust(largest + 2, ' '),
            operator + ' ' + bottom.rjust(largest, ' '),
            '-' * (largest + 2)
        )

        # And if it's been solved, add in a fourth.
        if final:
            t = (*t, str(final).rjust(largest + 2, ' '))
        # Collect the formatted lines into a list.
        formatted_problems.append(t)

    # Link together all the first lines, second lines, ----- bars
    # (and potentially solution lines) as a tuple.
    zipped = zip(*formatted_problems)
    # Space each problem's values by four spaces, then join them all into
    # one string with line separators.
    return '\n'.join([
      (' ' * 4).join(entry) for entry in zipped
      ])
