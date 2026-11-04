# Evaluation Methodology

This document describes the project scope, review approach, and the records available.

## Project question

How did the project owner judge whether generated image, video, and read-aloud audio outputs matched their prompts and met their quality expectations?

## Scope and materials

The owner generated and reviewed 16 outputs: six images (IMG-01–IMG-06), six videos (VID-01–VID-06), and four read-aloud audio clips (VOX-01–VOX-04). The owner confirmed that the IDs correspond to the prompt IDs.

- **Images:** Generated with ChatGPT image generation. Exact model/version, generation settings, and seed are unknown. The owner reports image dimensions of 1536 × 1024 or 1024 × 1536.
- **Videos:** Generated with Gemini. The owner identifies the model as Gemini Omni Flash (`gemini-omni-1.1-flash`). Clips are 10 seconds. The owner reports that the interface did not offer manual controls for duration, resolution, or frame rate.
- **Audio:** Generated with ElevenLabs Eleven v4 using “Roger - Laid-Back, Casual, Resonant” (voice ID `CwhRBWXzGAHq8TQ4Fs17`). The supplied settings screenshot shows language Auto, MP3 44.1 kHz / 128 kbps, and approximate slider positions for Stability and Similarity.

See the [asset manifest](../data/asset-manifest.csv) for model details and local file save times. Save times are not confirmed generation times. The owner confirmed public-sharing permission. The media files are not yet included in this repository.

## Review procedure

The project owner personally reviewed the outputs and supplied the scores and observations in [owner-ratings.csv](../ratings/owner-ratings.csv). Notes distinguish observable details from subjective impressions, such as whether an output “looks AI-generated.” No second reviewer independently assessed the media.

Audio was reviewed in a quiet place at comfortable volume using Apple EarPods. Image/video viewing conditions and exact review dates, session numbers, and time spent are marked not recorded in the [evaluation log](../ratings/evaluation-log.csv).

## Rating approach

The owner supplied one overall impression score from 1 to 5 and a qualitative note for each output. These are labeled **overall impression (owner-stated)**. They are holistic judgments, not separate scores for rubric criteria.

The modality rubrics in `rubrics/` were not applied criterion by criterion in this review. No per-criterion score, confidence value, or exact timestamp was inferred from a general comment. Comparison and calibration exercises were not conducted.

## Results summary

The owner's overall scores were:

- Images: one score of 1, three scores of 2, and two scores of 5.
- Videos: one score of 2, four scores of 3, and one score of 4.
- Read-aloud audio: four scores of 5.

These counts describe this small set of owner-reviewed outputs. They do not establish general performance of any model or service.

## Limitations

- One reviewer supplied all scores; there was no second reviewer or agreement check.
- Scores are holistic and subjective. Rubric criteria were not scored separately.
- The earlier list mentioned two versions of the “Quiet Morning” poster, while the supplied folder and current ratings contain six image IDs; whether a second poster output exists remains unconfirmed.
- Image model details and generation settings are unknown; some details for the other modalities are also unavailable.
- Local file save times do not establish generation times or review-session dates.
- Media files are not in the public repository, so visitors cannot inspect them beside the notes.
- No cross-model comparison, calibration exercise, or inferential statistical analysis was performed.

## Ownership

The project owner generated and reviewed the media and supplied the scores and observations recorded in this report.
