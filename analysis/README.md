# Optional Rating Summary

The script summarizes only rows that the project owner has entered in ratings/owner-ratings.csv. It does not rate media, identify flaws, choose a preferred output, or create evaluation rationales.

From the repository root, run:

    python analysis/summarize_ratings.py

To use another CSV:

    python analysis/summarize_ratings.py --input path/to/ratings.csv --output path/to/summary.csv

Rows must use the owner-ratings.csv column names. Only integer scores from 1 through 5 are included. Blank, uncertain, not-applicable, or invalid scores are excluded and counted separately in the status output. The script creates no summary file when there are no valid scores.

The output is a descriptive criterion-level summary (n, mean, median, minimum, maximum) grouped by module and criterion. It does not establish reliability, validity, model quality, or statistical significance. Interpret results in context and report limitations.
