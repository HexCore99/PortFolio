# Resume

The public download is `static/siabul-hassan-resume.pdf`. It is linked from the hero and contact section through `ResumeLink.svelte`.

To update it, edit the content in `scripts/build_resume.py`, then run:

```sh
python -m pip install reportlab pypdf
python scripts/build_resume.py
```

The generator creates `output/pdf/siabul-hassan-resume.pdf`, validates that it has one page and the expected text, and copies it to the public path. Render and visually inspect the PDF after content changes, then rebuild the website.

Content uses the portfolio's project descriptions and details supplied by Siabul. CGPA is shown as 3.90 without an unconfirmed grading scale. Employment history is omitted because no professional experience was reported. Review the trimester and expected graduation date when updating.
