# Multimodal AI Output Evaluation & Quality Assessment

This self-initiated portfolio project documents a human review of AI-generated images, videos, and read-aloud audio against written prompts.

## Project scope

The project owner generated and reviewed six images, six videos, and four read-aloud audio clips. Each output has an owner-provided overall score from 1 to 5 and a qualitative observation. The scores are holistic impressions, not separate scores for each rubric criterion.

The review covers prompt fit and perceived quality. It is a small, single-reviewer exercise; it does not establish general performance of the generation services. Pairwise comparisons and calibration were not performed.

## Summary of owner scores

| Modality | Outputs | Overall score distribution |
|---|---:|---|
| Images | 6 | 1: one; 2: three; 5: two |
| Videos | 6 | 2: one; 3: four; 4: one |
| Read-aloud audio | 4 | 5: four |

See the [results report](reports/final-evaluation-report.md) for the owner’s observations and limitations.

## Repository contents

- [Prompts](prompts/) — image, video, and voice prompt sets
- [Guidelines](guidelines/) — review principles and workflow
- [Rubrics](rubrics/) — criteria available for a more detailed second pass
- [Asset manifest](data/asset-manifest.csv) — tool details, settings, and file references
- [Images](data/assets/images/), [videos](data/assets/videos/), and [audio](data/assets/audio/) — reviewed media outputs
- [Owner ratings](ratings/owner-ratings.csv) and [evaluation log](ratings/evaluation-log.csv)
- [Methodology](reports/methodology.md) and [results report](reports/final-evaluation-report.md)

## Evaluation approach

The owner supplied all ratings and observations recorded in this repository. The rubric files provide useful criteria, but this review used a single overall score per output. It should therefore be described as a holistic review, not a criterion-by-criterion rubric assessment.

## Responsible use

The owner confirmed that these generated files may be shared publicly. The asset manifest records the tools and available provenance details. Local save times are not confirmed generation times.
