"""Render proposal.md to a letter-size PDF via headless Chrome and report the page count.

Usage: python3 -I scripts/make_pdf.py <proposal.md> <out.pdf> [font_pt]
"""
import pathlib
import subprocess
import sys
import tempfile

import markdown
import pypdf

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
font_pt = sys.argv[3] if len(sys.argv) > 3 else "11"

body = markdown.markdown(src.read_text(), extensions=["tables"])
css = f"""
@page {{ size: Letter; margin: 0.7in; }}
body {{ font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: {font_pt}pt;
       line-height: 1.3; color: #111; }}
h1 {{ font-size: 1.45em; margin: 0 0 0.15em; }}
h1 + p {{ color: #444; margin-top: 0; }}
h2 {{ font-size: 1.1em; margin: 0.9em 0 0.3em; border-bottom: 1px solid #bbb; padding-bottom: 2px; }}
p {{ margin: 0.35em 0; }}
ul, ol {{ margin: 0.3em 0; padding-left: 1.4em; }}
li {{ margin: 0.15em 0; }}
table {{ border-collapse: collapse; margin: 0.5em 0; }}
th, td {{ border: 1px solid #999; padding: 2px 10px; text-align: left; }}
td:last-child, th:last-child {{ text-align: right; }}
a {{ color: #1a4fa0; text-decoration: none; }}
"""
html = f"<!doctype html><html><head><meta charset='utf-8'><title>AIDA: Genome Center Focus Group Proposal</title><style>{css}</style></head><body>{body}</body></html>"

with tempfile.TemporaryDirectory(dir=out.parent) as tmp:
    page = pathlib.Path(tmp) / "proposal.html"
    page.write_text(html)
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", f"--user-data-dir={tmp}/profile",
         "--no-pdf-header-footer", f"--print-to-pdf={out}", page.as_uri()],
        check=True, capture_output=True, timeout=120,
    )

print(f"{out}: {len(pypdf.PdfReader(out).pages)} pages at {font_pt}pt")
