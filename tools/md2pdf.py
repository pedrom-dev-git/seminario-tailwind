#!/usr/bin/env python3
"""Converte artigo-tecnico.md -> artigo-tecnico.pdf (Markdown + WeasyPrint).

Uso:
    python3 tools/md2pdf.py

Sem args: usa artigo-tecnico.md na raiz do repo e gera artigo-tecnico.pdf ao lado.
Requer: markdown, weasyprint (já instalados nesta máquina).
"""
import pathlib
import sys

import markdown
from weasyprint import HTML

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC = REPO / "artigo-tecnico.md"
OUT = REPO / "artigo-tecnico.pdf"

CSS = """
@page { size: A4; margin: 2cm; }
body { font-family: 'DejaVu Sans', system-ui, sans-serif;
       font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 20pt; border-bottom: 2px solid #4f46e5; padding-bottom: .2em; }
h2 { font-size: 14pt; margin-top: 1.4em; color: #312e81; }
h3 { font-size: 12pt; margin-top: 1em; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt;
       background: #f3f4f6; padding: .1em .3em; border-radius: 3px; }
pre { background: #f3f4f6; padding: .8em; border-radius: 6px;
      font-size: 8.5pt; overflow-x: auto; white-space: pre-wrap; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 9.5pt; }
th, td { border: 1px solid #d1d5db; padding: .4em .6em; text-align: left; }
th { background: #eef2ff; }
blockquote { border-left: 3px solid #c7d2fe; margin: 1em 0; padding: .3em 1em;
             color: #4b5563; background: #fafafa; }
a { color: #4f46e5; word-break: break-all; }
"""


def main() -> int:
    if not SRC.exists():
        print(f"ERRO: não encontrei {SRC}", file=sys.stderr)
        return 1
    md_text = SRC.read_text(encoding="utf-8")
    body = markdown.markdown(
        md_text, extensions=["tables", "fenced_code", "sane_lists"]
    )
    html_doc = (
        f"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    HTML(string=html_doc).write_pdf(OUT)
    print(f"PDF gerado: {OUT} ({OUT.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
