from pathlib import Path
import json
import nbformat
import plotly.io as pio

NOTEBOOK = Path("DSA495-M06-Topic-Modeling.ipynb")
OUT = Path("generated")
OUT.mkdir(exist_ok=True)

targets = [
    ("visualize_barchart", "01-topic-word-bars"),
    ("visualize_documents", "02-document-map"),
    ("visualize_topics", "03-intertopic-distance-map"),
    ("visualize_hierarchy", "04-topic-hierarchy"),
]

nb = nbformat.read(NOTEBOOK, as_version=4)

found = {}
for cell in nb.cells:
    if cell.cell_type != "code":
        continue
    source = cell.source or ""
    target = next(((needle, name) for needle, name in targets if needle in source), None)
    if not target:
        continue
    needle, name = target
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        spec = data.get("application/vnd.plotly.v1+json")
        if spec:
            fig = pio.from_json(json.dumps(spec))
            fig.write_html(OUT / f"{name}.html", include_plotlyjs="cdn")
            fig.write_image(OUT / f"{name}.png", scale=1.5)
            found[name] = True
            break

missing = [name for _, name in targets if name not in found]
if missing:
    raise RuntimeError(f"Could not find Plotly outputs for: {missing}")

print("Exported:", ", ".join(sorted(found)))
